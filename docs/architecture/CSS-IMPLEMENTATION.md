# 🧱 SRAGI Ultimate CSS - Bricks Implementation Guide

**File:** `/docs/architecture/SRAGI-CSS-IMPLEMENTATION.md`

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 2.1 (SSOT Path Aligned)

**Status:** PRODUCTION STANDARD

**Compatible with:** Bricks Builder 2.1+

---

## 🎯 Implementation Steps

### Step 1: Create Child Theme (Mandatory)

# SSH to your server
cd /wp-content/themes/
mkdir bricks-child
cd bricks-child

Create `style.css`:
```css
/*
Theme Name: Bricks Child - SRAGI
Template: bricks
Version: 2.1
Description: SRAGI White Paper Edition
Author: Rune Solberg
*/
````

Create `functions.php`:

PHP

```
<?php
/** * SRAGI Bricks Child Theme 
 * Enqueue SRAGI CSS and Critical Path
 */
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'sragi-css',
        get_stylesheet_directory_uri() . '/sragi.css',
        array('bricks-frontend'),
        '2.1' // <-- BUMPED VERSION
    );
}, 20);
```

### **Step 2: Add SRAGI CSS**

Create `/wp-content/themes/bricks-child/sragi.css` and paste the entire `SRAGI Ultimate CSS v2.0`.

### **Step 3: Configure Bricks Theme Styles**

Go to: **Bricks → Settings → Theme Styles**

* **Colors (Must match `sragi.css` variables):**  
  * Primary: `var(--clr-link)`  
  * Background: `var(--clr-white)`  
  * Text: `var(--clr-black)`  
* **Typography:**  
  * Heading Font: `Georgia` (or `var(--ff-serif)`)  
  * Body Font: `System Sans` (or `var(--ff-sans)`)  
  * Base Size: `16px` (`clamp` for fluid type)

### **Step 4: Activate Child Theme**

Go to: **Appearance → Themes → Activate "Bricks Child \- SRAGI"**

---

## **🧩 Bricks-Specific Class Usage**

* **Containers:** Use predefined semantic widths for readability.  
  * `<div class="container-sm">` (Narrow article width)  
  * `<div class="container">` (Default content)  
* **Text:**  
  * `<p class="text-meta">` (Meta information)  
  * `<p class="text-caption">` (Figure captions)  
* **Academic Components:**  
  * `<div class="abstract">...</div>`  
  * `<div class="figure">...</div>`

---

## **🔧 Advanced: Design Tokens from YAML (SSOT Bridge)**

### **Option 2: WPCodeBox Auto-Generation (Recommended)**

This snippet reads the **SSOT** brand colors and exposes them as `:root` CSS variables.

PHP

```
<?php
/** * Generate CSS tokens from YAML 
 * Syncs SRAGI-BRAND-COLORS.yaml → :root CSS variables
 * NOTE: The path MUST be correct for your specific server/snippet environment.
 */
add_action('wp_head', function() {
    // ⚠️ CRITICAL PATH UPDATE: Must point to the Git-synced SSOT folder!
    $yaml_file = ABSPATH . 'wp-content/themes/bricks-child/docs/_CONFIG/SRAGI-BRAND-COLORS.yaml'; 
    
    if (!file_exists($yaml_file)) return;
    
    // Logic to parse YAML and output <style> block here...
    // [Implementation details omitted for conciseness in documentation]

    $colors = yaml_parse_file($yaml_file);
    
    echo '<style id="sragi-tokens">';
    echo ':root {';
    // Foundation, Grays, Accent loop logic...
    // foreach ($colors['foundation'] as $name => $data) { ... }
    echo '}';
    echo '</style>';
}, 5);
```

---

## **♿ Accessibility & Performance**

* **Accessibility Checklist:** Verify keyboard navigation, contrast ratios (WCAG AA minimum: 4.5:1), and screen reader compatibility.  
* **Performance:** Use `wp_enqueue_style` with version bumping for cache busting. Defer non-critical CSS using `rel='preload' as='style'` on `sragi-css`.

---

**© 2025 Rune Solberg / Neptunia Media AS** Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL). See SRL-LICENSE.yaml for current version and details.

