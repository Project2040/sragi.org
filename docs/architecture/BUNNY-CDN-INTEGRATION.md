# 🐇 SRAGI Bunny.net CDN Integration

**File:** `/docs/architecture/BUNNY-CDN-INTEGRATION.md`  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.0c  
**Status:** 🟡 Planning → Implementation  
**Target Completion:** Q1 2026  
**Last Updated:** October 29, 2025 (Marked for change, Rune Solberg, 06.12.2025)

# This file need a major update as this is now implemented!! (Rune Solberg, 06.12.2025)
---

## 🎯 Purpose

Integrate **Bunny.net CDN** into sragi.org for:
- ⚡ **Global performance** (edge caching)
- 🖼️ **Automatic image optimization** (WebP/AVIF)
- 🌍 **Reduced server load** (static asset offloading)
- 📊 **Better analytics** (bandwidth insights)

---

## 📋 Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| **Bunny Account** | ✅ Active | Account: neptunia-media |
| **Pull Zone Created** | ⏳ Pending | Target: `sragi.b-cdn.net` |
| **CNAME Setup** | ⏳ Pending | DNS: `media.sragi.org` |
| **WordPress Integration** | ⏳ Pending | URL rewrite filter |
| **Image Optimization** | ⏳ Pending | WebP/AVIF enabled |
| **Cache Purge Logic** | ⏳ Pending | Auto-purge on update |

---

## 🌊 Implementation Journey (Kairos Approach)

### Phase 1: Foundation

**Kairos Marker:** When WordPress and content structure feel ready for transformation

**Goal:** Prepare the field – create clarity before velocity

**Readiness Signals:**
- You feel confident in media organization
- Performance baseline is documented
- Team understands the *why*, not just the *how*
- Energy is present for systemic change

**Tasks:**
- [x] Define folder structure (`/content/`, `/visuals/`)
- [x] Audit existing media library
- [x] Optimize images with TinyPNG/SVGO
- [ ] Benchmark current site performance
  - Tools: GTmetrix, Lighthouse, Pingdom
  - Metrics: TTFB, LCP, CLS, Speed Index
- [ ] Document baseline performance
  - Create `/docs/performance/baseline-2025-10.md`

**Success Criteria:**
- ✅ All images under 500KB
- ✅ SVG diagrams optimized
- ✅ Baseline metrics documented

---

### Phase 2: CDN Deployment (Week 3-4)

**Goal:** Configure and connect Bunny.net CDN

#### Step 1: Create Pull Zone

**Bunny Dashboard:**
```
1. Go to: https://dash.bunny.net/
2. Pull Zones → Add Pull Zone
3. Settings:
   - Name: sragi-org
   - Origin URL: https://sragi.org/wp-content/uploads/
   - CDN URL: sragi.b-cdn.net
```

**Configuration:**
```yaml
pull_zone:
  name: sragi-org
  origin: https://sragi.org/wp-content/uploads/
  cdn_url: sragi.b-cdn.net
  
optimizer:
  enabled: true
  webp: true
  avif: true
  quality: 85
  
edge_rules:
  - match: "*.{jpg,jpeg,png,gif,svg,webp}"
    cache_ttl: 31536000  # 1 year
  - match: "*.{css,js}"
    cache_ttl: 86400     # 1 day
  - match: "*.pdf"
    cache_ttl: 604800    # 1 week
```

#### Step 2: DNS Configuration

**Add CNAME Record:**
```
Type:  CNAME
Host:  media
Value: sragi.b-cdn.net
TTL:   3600
```

**Result:**
```
https://media.sragi.org → https://sragi.b-cdn.net
```

#### Step 3: WordPress Integration

**Create WPCodeBox Snippet:**

File: `/wordpress/wpcodebox/sragi_bunny_cdn.php`

```php
<?php
/**
 * SRAGI Bunny.net CDN Integration
 * 
 * Rewrites all wp-content/uploads URLs to Bunny CDN
 * Includes cache purge functionality
 * 
 * @package SRAGI
 * @version 1.0
 */

// ===========================================================
// CONFIGURATION
// ===========================================================

// Enable/disable CDN (set in wp-config.php)
// define('SRAGI_CDN_ENABLED', true);
// define('BUNNY_API_KEY', 'your-api-key-here');
// define('BUNNY_PULL_ZONE_ID', 'your-pull-zone-id');

define('SRAGI_CDN_URL', 'https://media.sragi.org');
define('SRAGI_ORIGIN_URL', 'https://sragi.org/wp-content/uploads');

// ===========================================================
// URL REWRITING
// ===========================================================

/**
 * Rewrite attachment URLs to CDN
 */
add_filter('wp_get_attachment_url', 'sragi_cdn_rewrite_url', 10, 2);

function sragi_cdn_rewrite_url($url, $post_id = null) {
    // Check if CDN is enabled
    if (!defined('SRAGI_CDN_ENABLED') || !SRAGI_CDN_ENABLED) {
        return $url;
    }
    
    // Only rewrite uploads directory
    if (strpos($url, '/wp-content/uploads/') === false) {
        return $url;
    }
    
    return str_replace(SRAGI_ORIGIN_URL, SRAGI_CDN_URL, $url);
}

/**
 * Rewrite srcset URLs for responsive images
 */
add_filter('wp_calculate_image_srcset', 'sragi_cdn_rewrite_srcset', 10, 5);

function sragi_cdn_rewrite_srcset($sources, $size_array, $image_src, $image_meta, $attachment_id) {
    if (!defined('SRAGI_CDN_ENABLED') || !SRAGI_CDN_ENABLED) {
        return $sources;
    }
    
    foreach ($sources as &$source) {
        $source['url'] = str_replace(SRAGI_ORIGIN_URL, SRAGI_CDN_URL, $source['url']);
    }
    
    return $sources;
}

// ===========================================================
// CACHE PURGING
// ===========================================================

/**
 * Purge Bunny CDN cache for specific URLs
 * 
 * @param string|array $urls URLs to purge
 * @return bool Success status
 */
function sragi_bunny_purge_cache($urls) {
    // Check credentials
    if (!defined('BUNNY_API_KEY') || !defined('BUNNY_PULL_ZONE_ID')) {
        error_log('SRAGI: Bunny CDN credentials not configured');
        return false;
    }
    
    $api_key = BUNNY_API_KEY;
    $pull_zone_id = BUNNY_PULL_ZONE_ID;
    
    // Ensure array
    if (!is_array($urls)) {
        $urls = [$urls];
    }
    
    $success = true;
    
    foreach ($urls as $url) {
        $response = wp_remote_post(
            "https://api.bunny.net/pullzone/{$pull_zone_id}/purgeCache",
            [
                'headers' => [
                    'AccessKey' => $api_key,
                    'Content-Type' => 'application/json',
                ],
                'body' => json_encode(['url' => $url]),
                'timeout' => 10,
            ]
        );
        
        if (is_wp_error($response)) {
            error_log('SRAGI Bunny purge failed: ' . $response->get_error_message());
            $success = false;
        } else {
            error_log('SRAGI Bunny purged: ' . $url);
        }
    }
    
    return $success;
}

/**
 * Auto-purge cache when post/page is updated
 */
add_action('save_post', 'sragi_auto_purge_post', 10, 3);

function sragi_auto_purge_post($post_id, $post, $update) {
    // Skip for revisions
    if (wp_is_post_revision($post_id)) {
        return;
    }
    
    // Skip if not published
    if ($post->post_status !== 'publish') {
        return;
    }
    
    // Get post URL and featured image
    $urls_to_purge = [get_permalink($post_id)];
    
    // Add featured image if exists
    $thumbnail_id = get_post_thumbnail_id($post_id);
    if ($thumbnail_id) {
        $thumbnail_url = wp_get_attachment_url($thumbnail_id);
        if ($thumbnail_url) {
            $urls_to_purge[] = $thumbnail_url;
        }
    }
    
    // Purge cache
    sragi_bunny_purge_cache($urls_to_purge);
}

/**
 * Manual cache purge button (admin only)
 */
add_action('admin_bar_menu', 'sragi_add_purge_button', 100);

function sragi_add_purge_button($wp_admin_bar) {
    if (!current_user_can('manage_options')) {
        return;
    }
    
    $wp_admin_bar->add_node([
        'id'    => 'sragi-purge-cache',
        'title' => '🐇 Purge CDN Cache',
        'href'  => wp_nonce_url(admin_url('admin-post.php?action=sragi_purge_all_cache'), 'sragi_purge_cache'),
    ]);
}

/**
 * Handle manual purge request
 */
add_action('admin_post_sragi_purge_all_cache', 'sragi_handle_manual_purge');

function sragi_handle_manual_purge() {
    // Verify nonce
    if (!wp_verify_nonce($_GET['_wpnonce'], 'sragi_purge_cache')) {
        wp_die('Invalid request');
    }
    
    // Check permissions
    if (!current_user_can('manage_options')) {
        wp_die('Insufficient permissions');
    }
    
    // Purge homepage
    $success = sragi_bunny_purge_cache(home_url('/'));
    
    // Redirect back with message
    $redirect = add_query_arg([
        'message' => $success ? 'cache_purged' : 'cache_purge_failed',
    ], wp_get_referer());
    
    wp_safe_redirect($redirect);
    exit;
}
```

**Enable in wp-config.php:**
```php
// Bunny CDN Configuration
define('SRAGI_CDN_ENABLED', true);
define('BUNNY_API_KEY', 'your-bunny-api-key-here');
define('BUNNY_PULL_ZONE_ID', 'your-pull-zone-id-here');
```

#### Step 4: Testing

**Test URLs:**
```
Before: https://sragi.org/wp-content/uploads/2025/10/logo.png
After:  https://media.sragi.org/2025/10/logo.png
```

**Verification:**
```bash
# Check if CDN is serving
curl -I https://media.sragi.org/2025/10/logo.png

# Should see:
# X-Cache: HIT
# Server: BunnyCDN
```

**Success Criteria:**
- ✅ Images load from `media.sragi.org`
- ✅ HTTP headers show Bunny cache
- ✅ Page load time improved
- ✅ No broken images

---

### Phase 3: Optimization (Week 5-6)

**Goal:** Fine-tune performance and automation

**Tasks:**
- [ ] Enable WebP/AVIF auto-conversion
- [ ] Configure cache TTL rules
- [ ] Set up Bunny Analytics dashboard
- [ ] Implement lazy loading for images
- [ ] Configure preload hints for critical assets
- [ ] Monitor bandwidth usage
- [ ] Document performance improvements

**Monitoring:**
```
Weekly checks:
- Bandwidth usage (Bunny Dashboard)
- Cache hit ratio (target: >90%)
- Image optimization stats
- Page speed scores (GTmetrix)
```

**Success Criteria:**
- ✅ Cache hit ratio >90%
- ✅ LCP improved by 30%+
- ✅ Bandwidth reduced by 50%+
- ✅ All images auto-converted to WebP

---

## 📊 Performance Targets

| Metric | Before CDN | Target | Measurement |
|--------|-----------|--------|-------------|
| **TTFB** | TBD | <200ms | GTmetrix |
| **LCP** | TBD | <2.5s | Lighthouse |
| **CLS** | TBD | <0.1 | Lighthouse |
| **Speed Index** | TBD | <3s | GTmetrix |
| **Total Page Size** | TBD | <1MB | DevTools |
| **Cache Hit Ratio** | N/A | >90% | Bunny Dashboard |

---

## 💰 Cost Estimate

**Bunny.net Pricing (Pay-as-you-go):**
```
Storage:    $0.01/GB/month
Bandwidth:  $0.01-0.05/GB (region dependent)
Requests:   $1.00/million requests
```

**Expected Monthly Cost:**
```
Storage:    10 GB × $0.01 = $0.10
Bandwidth:  100 GB × $0.01 = $1.00
Requests:   1M × $0.001 = $1.00
---
Total:      ~$2-5/month
```

**Comparison:**
- Bunny.net: $2-5/month
- Cloudflare: $20/month (Pro)
- AWS CloudFront: $10-50/month

**Savings:** ~80% vs alternatives

---

## 🔧 Configuration Reference

### Bunny Dashboard Settings

**Optimizer:**
```
✅ Enable Optimizer
✅ WebP Conversion
✅ AVIF Conversion
   Quality: 85
✅ Automatic Mobile Optimization
✅ Lazy Loading
```

**Caching:**
```
✅ Enable CDN
   Cache TTL: 1 year (images)
   Browser Cache: 1 year
✅ Query String Handling: Ignore
✅ Vary Header: Accept-Encoding
```

**Security:**
```
✅ Token Authentication: Disabled (public assets)
✅ Geo-blocking: Disabled
✅ Hotlink Protection: Enabled
   Allowed domains: sragi.org, neptuniamedia.org
```

### WordPress Settings

**WPCodeBox Snippet:**
```
Name: SRAGI Bunny CDN
Type: PHP
Location: Global (all pages)
Status: Active
```

**wp-config.php:**
```php
define('SRAGI_CDN_ENABLED', true);
define('BUNNY_API_KEY', '[secret]');
define('BUNNY_PULL_ZONE_ID', '[id]');
```

---

## 📚 Related Documentation

- [SRAGI Conventions](../docs/SRAGI-CONVENTIONS.md)
- [SRAGI Image Guidelines](../assets/docs/image-guidelines.md)
- [SRAGI Architecture](../ARCHITECTURE.md)
- [Bunny.net Official Docs](https://docs.bunny.net/)

---

## 🐛 Troubleshooting

### Images Not Loading from CDN

**Symptoms:** Images still load from origin

**Check:**
1. Is `SRAGI_CDN_ENABLED` set to `true`?
2. Is WPCodeBox snippet active?
3. Clear browser cache
4. Check WordPress debug.log for errors

### Cache Not Purging

**Symptoms:** Old images still showing

**Check:**
1. Are `BUNNY_API_KEY` and `BUNNY_PULL_ZONE_ID` correct?
2. Check WordPress error logs
3. Manually purge via Bunny Dashboard
4. Verify webhook/action triggers

### Poor Cache Hit Ratio

**Symptoms:** Cache hit ratio <70%

**Solutions:**
1. Increase cache TTL
2. Check for dynamic query strings
3. Review Vary headers
4. Enable "Ignore Query String" in Bunny

---

## ✅ Completion Checklist

- [ ] Phase 1: Foundation complete
- [ ] Phase 2: CDN deployed and tested
- [ ] Phase 3: Optimizations implemented
- [ ] Performance targets met
- [ ] Documentation updated
- [ ] Team trained on cache purging
- [ ] Monitoring dashboard set up
- [ ] Backup/rollback plan documented

---

## 📞 Support

**Bunny.net Support:**
- 📧 support@bunny.net
- 💬 https://support.bunny.net/

**SRAGI Team:**
- 📧 kontakt@sragi.org
- 🌐 https://sragi.org

---

**© 2025 Rune Solberg / Neptunia Media AS**  
Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL) v1.0

---

*"Speed is not velocity without direction."*  
— SRAGI Performance Philosophy
