# **🐇 SRAGI Bunny.net CDN Integration (Master Guide)**

File: /docs/architecture/BUNNY-CDN-INTEGRATION.md

Maintainer: Rune Solberg / Neptunia Media AS

Version: 2.2 (Complete Implementation Guide)

Status: ✅ PRODUCTION ACTIVE

Platform: One.com Guru \+ WordPress \+ Bunny.net

Last Updated: January 2026

---

## **🎯 Purpose**

Integrate **Bunny.net CDN** into sragi.org (and future Neptunia sites) to achieve:

* ⚡ **Edge Performance:** Serve media from global nodes closer to the user.  
* 🖼️ **Asset Offloading:** Reduce load on the One.com origin server.  
* 💰 **Lean Cost Structure:** Using local optimization pipeline (no paid CDN add-ons).  
* 🔐 **SSOT Compliance:** Configuration via code (wp-config.php), not database settings.)

---

## **📋 System Status**

| Component | Status | Configuration |
| :---- | ----- | ----- |
| Bunny Account | ✅ Active | Rune Solberg, bruker@info-nett.no, firma Neptunia Media AS |
| Pull Zone | ✅ Active | sragi-org (Standard Tier) |
| Hostname | ✅ Active | [https://media.sragi.org](https://media.sragi.org/) |
| WordPress Bridge | ✅ Active | Custom PHP Rewrite (WPCodeBox) |

---

## **🏗️ Architecture Overview**

| Component | Setting | Value / Note |
| :---- | :---- | :---- |
| **Origin Strategy** | **Root Origin** | CDN points to https://www.sragi.org (allows caching CSS/JS later). |
| **URL Rewriting** | **Uploads Path** | Rewrites /wp-content/uploads/ to media.sragi.org/wp-content/uploads/. |
| **Optimization** | **Local Pipeline** | We upload optimized AVIF. Bunny Optimizer is **DISABLED** to save costs. |
| **SSL** | **Full** | media.sragi.org secured via Let's Encrypt in Bunny. |

---

## 

## **🛠️ Step-by-Step Implementation Guide**

### **1\. Bunny.net Configuration**

1. **Create Pull Zone:**  
   * Name: sragi-org (becomes sragi-org.b-cdn.net).  
   * Origin URL: https://www.sragi.org (**Note:** Point to root, not uploads).  
   * Pricing Tier: Standard.

2. **Add Hostname:**  
   * Add media.sragi.org.  
   * Enable SSL (Let's Encrypt).

3. **Disable Optimizer:**  
   * Ensure "Bunny Optimizer" is **OFF** (We optimize locally).

---

### **2\. DNS Setup (One.com Control Panel)**

*Critical step to link media.sragi.org to Bunny.*

1. Log in to **One.com** → **DNS Settings**.  
2. Create a new record under **DNS records**:  
   * **Type:** CNAME  
   * **Hostname (Alias):** media  
   * **Value (Target):** sragi-org.b-cdn.net (Check your specific Bunny hostname).  
   * **TTL:** 3600 (1 hour).  
3. Click **Create record**.  
4. *Wait 15-60 minutes for propagation.*

---

### **3\. Server Configuration (wp-config.php)**

*This file activates the logic. It keeps credentials out of the database.*

1. Access server via **SFTP** or **One.com File Manager**.  
2. Edit wp-config.php in the root folder.  
3. Add this block **above** /\* That's all, stop editing\! \*/:

PHP

```
// ===========================================================
// 🐰 SRAGI BUNNY CDN CONFIGURATION
// ===========================================================
// Master Switch
define('SRAGI_CDN_ENABLED', true);

// Purge Credentials (Get from Bunny Dashboard -> Account / Pull Zone)
define('BUNNY_API_KEY', 'ditt-lange-api-passord-her'); 
define('BUNNY_PULL_ZONE_ID', 'din-id-her'); // ID from Pull Zone Overview

// URL Definitions (The "Root Origin" Strategy)
// Note: We include the full path to align the rewrite logic accurately.
define('SRAGI_CDN_URL', 'https://media.sragi.org/wp-content/uploads');
define('SRAGI_ORIGIN_URL', 'https://www.sragi.org/wp-content/uploads');
```

---

### **4\. WordPress Integration (The Bridge Logic)**

*The engine that rewrites the URLs on the fly.*

Tool: WPCodeBox (or functions.php).

Snippet Name: SRAGI Bunny CDN Bridge.

Type: PHP (Run everywhere).

PHP

```
<?php
/*
Snippet Name: SRAGI Bunny CDN Integration (Robust)
Description: Advanced rewriting to Bunny CDN with dynamic origin, type safety, and auto-purge.
Version: 2.3 (Robust Edition)
Author: Rune Solberg / Neptunia Media AS
License: CC BY-SA 4.0 via SRL
*/

// ===========================================================
// 1. KONFIGURASJON & HJELPERE
// ===========================================================

if (!defined('SRAGI_CDN_URL')) {
    // VIKTIG: Pek denne mot mappen i Bunny hvis du bruker root-origin strategi
    define('SRAGI_CDN_URL', 'https://media.sragi.org/wp-content/uploads');
}

// Fallback hvis WP ikke klarer å finne egen upload-dir
if (!defined('SRAGI_ORIGIN_URL')) {
    define('SRAGI_ORIGIN_URL', 'https://www.sragi.org/wp-content/uploads');
}

function sragi_cdn_enabled(): bool {
    return (defined('SRAGI_CDN_ENABLED') && SRAGI_CDN_ENABLED);
}

// Henter den FAKTISKE URL-en til opplastinger dynamisk
function sragi_origin_baseurl(): string {
    $uploads = wp_upload_dir(null, false);
    if (!empty($uploads['baseurl'])) {
        return rtrim($uploads['baseurl'], '/');
    }
    return rtrim(SRAGI_ORIGIN_URL, '/');
}

function sragi_cdn_baseurl(): string {
    return rtrim(SRAGI_CDN_URL, '/');
}

// ===========================================================
// 2. URL REWRITING (Motoren)
// ===========================================================

add_filter('wp_get_attachment_url', 'sragi_cdn_rewrite_url', 10, 2);

function sragi_cdn_rewrite_url($url, $post_id = null) {
    // Fail-fast sjekker
    if (!sragi_cdn_enabled() || !is_string($url) || $url === '') return $url;

    // Kun påvirke filer i uploads-mappen
    if (strpos($url, '/wp-content/uploads/') === false) return $url;

    $origin = sragi_origin_baseurl();
    $cdn    = sragi_cdn_baseurl();

    // 1. Unngå dobbel rewrite (hvis URL allerede er CDN)
    if (strpos($url, $cdn) === 0) return $url;

    // 2. Hvis URL starter med origin (det vanlige tilfellet)
    if (strpos($url, $origin) === 0) {
        return $cdn . substr($url, strlen($origin));
    }

    // 3. Fallback: Prøv hardkodet replace hvis dynamisk feilet
    return str_replace(rtrim(SRAGI_ORIGIN_URL, '/'), $cdn, $url);
}

/**
 * Rewrite SRCSET (Responsive bilder)
 */
add_filter('wp_calculate_image_srcset', 'sragi_cdn_rewrite_srcset', 10, 5);

function sragi_cdn_rewrite_srcset($sources, $size_array, $image_src, $image_meta, $attachment_id) {
    if (!sragi_cdn_enabled() || !is_array($sources)) return $sources;

    $origin = sragi_origin_baseurl();
    $cdn    = sragi_cdn_baseurl();

    foreach ($sources as &$source) {
        if (!isset($source['url']) || !is_string($source['url'])) continue;

        // Skip hvis allerede CDN
        if (strpos($source['url'], $cdn) === 0) continue;

        if (strpos($source['url'], $origin) === 0) {
            $source['url'] = $cdn . substr($source['url'], strlen($origin));
        } else {
            $source['url'] = str_replace(rtrim(SRAGI_ORIGIN_URL, '/'), $cdn, $source['url']);
        }
    }
    return $sources;
}

// ===========================================================
// 3. CACHE PURGING (Renholdet)
// ===========================================================

function sragi_bunny_purge_cache($urls) {
    if (!defined('BUNNY_API_KEY') || !defined('BUNNY_PULL_ZONE_ID')) {
        return false;
    }

    if (!is_array($urls)) $urls = [$urls];

    $origin = sragi_origin_baseurl();
    $cdn    = sragi_cdn_baseurl();

    foreach ($urls as $url) {
        if (!is_string($url) || $url === '') continue;

        // Sørg for at vi purger CDN-urlen, ikke origin-urlen
        $cdn_url = $url;

        if (strpos($cdn_url, $cdn) !== 0) {
            if (strpos($cdn_url, $origin) === 0) {
                $cdn_url = $cdn . substr($cdn_url, strlen($origin));
            } else {
                $cdn_url = str_replace(rtrim(SRAGI_ORIGIN_URL, '/'), $cdn, $cdn_url);
            }
        }

        // Send API-kall (Async/Non-blocking for hastighet)
        wp_remote_post(
            "https://api.bunny.net/pullzone/" . BUNNY_PULL_ZONE_ID . "/purgeCache",
            [
                'headers' => [
                    'AccessKey' => BUNNY_API_KEY,
                    'Content-Type' => 'application/json',
                ],
                'body' => wp_json_encode(['url' => esc_url_raw($cdn_url)]),
                'timeout' => 5,
                'blocking' => false,
            ]
        );
    }
    return true;
}

// ===========================================================
// 4. ADMIN & AUTOMATIKK
// ===========================================================

// Legg til knapp i admin bar
add_action('admin_bar_menu', 'sragi_add_purge_button', 100);

function sragi_add_purge_button($wp_admin_bar) {
    if (!current_user_can('manage_options')) return;

    $wp_admin_bar->add_node([
        'id'    => 'sragi-purge-cache',
        'title' => '🐇 Purge CDN',
        'href'  => wp_nonce_url(admin_url('admin-post.php?action=sragi_purge_all'), 'sragi_purge')
    ]);
}

// Håndter manuell purge
add_action('admin_post_sragi_purge_all', 'sragi_handle_manual_purge');

function sragi_handle_manual_purge() {
    $nonce = $_GET['_wpnonce'] ?? '';

    if (!current_user_can('manage_options') || !wp_verify_nonce($nonce, 'sragi_purge')) {
        wp_die('Ingen tilgang.');
    }

    if (!defined('BUNNY_API_KEY') || !defined('BUNNY_PULL_ZONE_ID')) {
        wp_die('Mangler API-nøkler i wp-config.php');
    }

    // Purge hele sonen (Purge All)
    wp_remote_post(
        "https://api.bunny.net/pullzone/" . BUNNY_PULL_ZONE_ID . "/purgeCache",
        [
            'headers' => ['AccessKey' => BUNNY_API_KEY],
            'timeout' => 5
        ]
    );

    wp_safe_redirect(add_query_arg(['sragi_purged' => 1], wp_get_referer()));
    exit;
}

// Auto-purge ved lagring
add_action('save_post', 'sragi_auto_purge_on_save', 10, 3);

function sragi_auto_purge_on_save($post_id, $post, $update) {
    if (!sragi_cdn_enabled()) return;

    // Viktig: Unngå purge på autosave og revisjoner
    if (wp_is_post_revision($post_id) || wp_is_post_autosave($post_id)) return;
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) return;
    if (!is_object($post) || $post->post_status !== 'publish') return;

    $thumb_id = get_post_thumbnail_id($post_id);
    if ($thumb_id) {
        $url = wp_get_attachment_url($thumb_id);
        if ($url) sragi_bunny_purge_cache($url);
    }
}

// Auto-purge ved sletting
add_action('delete_attachment', 'sragi_auto_purge_on_delete');

function sragi_auto_purge_on_delete($post_id) {
    if (!sragi_cdn_enabled()) return;

    $url = wp_get_attachment_url($post_id);
    if ($url) sragi_bunny_purge_cache($url);
}

```

---

## **📊 Verification Checklist**

1. **Check Image URLs:** Right-click an image on the site.  
   * Start with: https://media.sragi.org/... ✅

2. **Check Headers:** Inspect Network tab in DevTools.  
   * x-cache: HIT or MISS (shows Bunny is active).  
   * server: BunnyCDN.

3. **Mobile Check:** Ensure images load on phones (validates srcset logic).

---

## **🆘 Troubleshooting**

**Images Broken (404)?**

* Check wp-config.php: Did you include /wp-content/uploads in both URL constants?  
* Check DNS: Has media.sragi.org propagated? (Use whatsmydns.net).

**Changes not showing?**

* Go to Bunny Dashboard \-\> **Purge Cache** (Purge All) to force a refresh.

---

© 2026 Rune Solberg / Neptunia Media AS

Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL).



