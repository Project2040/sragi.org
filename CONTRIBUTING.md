# Contributing

Identify the target artifact and its existing license before submitting changes. Supply authorship, source and third-party provenance. The presence of an open license does not by itself give Neptunia Media AS authority to offer a contributor's work under alternative commercial terms.

For commercial dual licensing, record sufficient permission through the applicable agreement or other rights instrument. [SRAGI_CLA.md](content/license/SRAGI_CLA.md) explains the rights-chain process; it is a notice and does not substitute for an executed agreement.

Run the repository checks before opening a pull request:

```sh
python -m pip install -r automation/license_builder/requirements.txt
python automation/license_builder/build_licenses.py
python automation/license_builder/build_licenses.py --check
python tools/enforce_version_refs.py
python -m unittest discover -s tests
```

Edit `SRL-LICENSE.yaml` before regenerating licensing outputs. Do not edit generated policy files independently. Preserve artifact-specific notices and previously granted rights. Record conflicting notices for review instead of silently choosing a new license.

Licensing contact: licensing@sragi.org.
