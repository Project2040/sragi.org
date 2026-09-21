"""Shared license resolution and typed content-template expansion.

Policy values live in the master. Syntax and precedence checks live here.
"""
import copy
from pathlib import Path
import re
from urllib.parse import urlsplit
import yaml

TOKEN = re.compile(r'{{\s*([\w.]+)\s*}}')


def at(context, dotted):
    value = context
    for key in dotted.split('.'):
        if not isinstance(value, dict) or key not in value:
            raise ValueError(f'Missing template value: {dotted}')
        value = value[key]
    return value


def expand(value, context):
    if isinstance(value, dict):
        return {key: expand(item, context) for key, item in value.items()}
    if isinstance(value, list):
        return [expand(item, context) for item in value]
    if not isinstance(value, str):
        return value
    match = TOKEN.fullmatch(value)
    if match:
        return copy.deepcopy(at(context, match[1]))
    value = TOKEN.sub(lambda match: str(at(context, match[1])), value)
    if '{{' in value or '}}' in value:
        raise ValueError('Unresolved content-template placeholder')
    return value


def resolve_license(data, supplied, profile, publication, require_resolved=False):
    """An explicit notice wins; website inheritance needs a verified scope.

    This validates metadata supplied to the content tool, not the live CMS.
    Legacy `type` is accepted as input but must not conflict with SPDX.
    """
    result = copy.deepcopy(supplied or {})
    expressions = {result[key] for key in ('spdx', 'type') if result.get(key)}
    if len(expressions) > 1:
        raise ValueError('Conflicting explicit license values')
    result.pop('type', None)
    result['spdx'] = next(iter(expressions), None)
    terms = result.get('rights_statement')
    if result['spdx'] or terms:
        result['status'] = 'explicit'
        result['resolved_from'] = 'artifact'
    else:
        parsed = urlsplit(publication.get('url', ''))
        origin = f'{parsed.scheme}://{parsed.netloc}'
        site = data['website_licensing']
        eligible = (profile == 'website_content' and origin in site['origins']
                    and publication.get('public') is True
                    and publication.get('rights_verified') is True
                    and publication.get('third_party', False) is False)
        if eligible:
            result.update(spdx=site['default_spdx'], status='inherited',
                          resolved_from='website_licensing', policy_url=site['policy_url'])
        else:
            result.update(status='unresolved', resolved_from=None)
    if require_resolved and result['status'] == 'unresolved':
        raise ValueError('Publication requires artifact terms or verified website-default eligibility')
    return result


def render_content(root, data, template_name, inputs, require_resolved=False):
    spec = data['content_templates'][template_name]
    path = (root / spec['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Template must stay in the repository')
    template = yaml.safe_load(path.read_text(encoding='utf-8'))
    context = dict(data, input=inputs)
    result = expand(template, context)
    # Explicit values supplied by the author override template placeholders.
    supplied = dict(result.get('license', {}), **inputs.get('license', {}))
    result['license'] = resolve_license(data, supplied,
                                        spec['profile'], inputs.get('publication_context', {}),
                                        require_resolved)
    return yaml.safe_dump(result, sort_keys=False, allow_unicode=True)


def validate_content_templates(root, data):
    """Ensure templates can express policy inheritance without embedding a grant."""
    for spec in data['content_templates'].values():
        path = (root / spec['path']).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('Template must stay in the repository')
        template = yaml.safe_load(path.read_text(encoding='utf-8'))
        license_info = template.get('license', {})
        if license_info.get('spdx') is not None or license_info.get('type'):
            raise ValueError(f'Content template embeds a license choice: {path}')
        if template.get('origin', {}).get('license'):
            raise ValueError(f'Visual template embeds a license choice: {path}')
        if license_info.get('policy_ref') != spec['profile']:
            raise ValueError(f'Content template policy differs from master: {path}')
