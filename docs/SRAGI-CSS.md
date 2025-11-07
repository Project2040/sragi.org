# 🧱 SRAGI Ultimate CSS - Bricks Implementation Guide

**Version:** 2.0  
**Author:** Rune Solberg / Neptunia Media AS  
**Last Updated:** October 29, 2025  
**Compatible with:** Bricks Builder 2.1+

---

## 🎯 Implementation Steps

### **Step 1: Create Child Theme**

```bash
# SSH to your server
cd /wp-content/themes/
mkdir bricks-child
cd bricks-child
```

Create `style.css`:
```css
/*
Theme Name: Bricks Child - SRAGI
Template: bricks
Version: 1.0
Description: SRAGI White Paper Edition
Author: Rune Solberg
*/
```

Create `functions.php`:
```php
<?php
/**
 * SRAGI Bricks Child Theme
 */

// Enqueue SRAGI CSS
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'sragi-css',
        get_stylesheet_directory_uri() . '/sragi.css',
        array('bricks-frontend'),
        '2.0'
    );
}, 20);
```

---

### **Step 2: Add SRAGI CSS**

Create `/wp-content/themes/bricks-child/sragi.css` and paste the entire **SRAGI Ultimate CSS v2.0**.

---

### **Step 3: Configure Bricks Theme Styles**

Go to: **Bricks → Settings → Theme Styles**

#### **Colors:**
```yaml
Primary:     var(--clr-link)
Background:  var(--clr-white)
Text:        var(--clr-black)
Muted:       var(--clr-gray-medium)
Border:      var(--clr-gray-light)
```

#### **Typography:**
```yaml
Heading Font: Georgia (or --ff-serif)
Body Font:    System Sans (or --ff-sans)
Line Height:  1.65
Base Size:    16px (clamp to 18px)
```

#### **Spacing:**
```yaml
Section Padding: 2rem (vertical)
Container Width: 52rem (832px)
Grid Gap:        1.5rem
```

---

### **Step 4: Activate Child Theme**

Go to: **Appearance → Themes → Activate "Bricks Child - SRAGI"**

---

## 🧩 Bricks-Specific Class Usage

### **Container Widths:**
```html
<!-- Narrow article -->
<div class="brxe-container container-sm">...</div>

<!-- Default content -->
<div class="brxe-container container">...</div>

<!-- Wide layout -->
<div class="brxe-container container-lg">...</div>
```

### **Typography:**
```html
<!-- Meta information -->
<p class="text-meta">Last updated: October 29, 2025</p>

<!-- Muted secondary text -->
<p class="text-muted">This is supplementary information.</p>

<!-- Caption -->
<p class="text-caption">Figure 1: SRAGI Architecture</p>
```

### **Academic Components:**
```html
<!-- Abstract -->
<div class="abstract">
  This paper presents the SRAGI framework...
</div>

<!-- Figure -->
<div class="figure">
  <img src="diagram.svg" alt="SRAGI Sync Loop">
  <p class="figure-caption">The SRAGI synchronization architecture</p>
</div>

<!-- Card -->
<div class="card">
  <h3>Key Insight</h3>
  <p>Content here...</p>
</div>
```

---

## 🎨 Creating Custom Bricks Elements

### **Example: Header Section**

**Bricks Structure:**
```
Section (ID: header)
  └─ Container
      ├─ Block (logo-section)
      │   ├─ Image (logo)
      │   └─ Text (SRAGI)
      └─ Block (header-right)
          ├─ Text (Regenerative AI)
          └─ Text (License link)
```

**Custom CSS in Bricks:**
```css
/* Section Settings */
#header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  padding-block: var(--space-xs);
}

/* Logo section */
.logo-section {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
}
```

---

## 🔧 Advanced: Design Tokens from YAML

### **Option 1: Manual Sync**

Update `:root` variables in `sragi.css` when `SRAGI-BRAND-COLORS.yaml` changes.

### **Option 2: WPCodeBox Auto-Generation (Recommended)**

Create snippet: `sragi_generate_css_tokens.php`

```php
<?php
/**
 * Generate CSS tokens from YAML
 * Syncs SRAGI-BRAND-COLORS.yaml → :root CSS variables
 */

add_action('wp_head', function() {
    $yaml_file = '/path/to/SRAGI-BRAND-COLORS.yaml';
    
    if (!file_exists($yaml_file)) return;
    
    $colors = yaml_parse_file($yaml_file);
    
    echo '<style id="sragi-tokens">';
    echo ':root {';
    
    // Foundation
    foreach ($colors['foundation'] as $name => $data) {
        $var_name = '--clr-' . str_replace('_', '-', $name);
        echo "{$var_name}: {$data['hex']}; ";
    }
    
    // Grays
    foreach ($colors['grays'] as $name => $data) {
        $var_name = '--clr-gray-' . $name;
        echo "{$var_name}: {$data['hex']}; ";
    }
    
    // Accent
    foreach ($colors['accent'] as $name => $data) {
        $var_name = '--clr-' . str_replace('_', '-', $name);
        echo "{$var_name}: {$data['hex']}; ";
    }
    
    echo '}';
    echo '</style>';
}, 5);
```

---

## 📐 Typography Presets for Bricks

Create these as **Bricks → Templates → Typography Presets**:

### **Preset: White Paper H1**
```yaml
Font Family:     Georgia
Font Size:       clamp(1.75rem, 1.5rem + 0.625vw, 2rem)
Font Weight:     700
Line Height:     1.2
Letter Spacing:  -0.01em
Margin Bottom:   0.5em
```

### **Preset: White Paper Body**
```yaml
Font Family:     System Sans
Font Size:       clamp(1rem, 0.95rem + 0.25vw, 1.125rem)
Font Weight:     400
Line Height:     1.65
Color:           var(--text)
```

### **Preset: Meta Text**
```yaml
Font Family:     System Sans
Font Size:       0.875rem
Font Weight:     400
Color:           var(--text-muted)
```

---

## 🌐 Responsive Adjustments

The CSS uses `clamp()` for fluid typography, but you can override in Bricks:

**Mobile Portrait (`max-width: 48rem`):**
```css
.brxe-section {
  padding-block: 1.5rem !important;
}

.container {
  max-width: calc(100% - 1rem);
}

h1 {
  font-size: 1.5rem;
}
```

---

## ♿ Accessibility Checklist

Before launching:
- [ ] Test keyboard navigation (Tab through all links)
- [ ] Verify contrast ratios (WCAG AA minimum: 4.5:1)
- [ ] Test with screen reader (NVDA/VoiceOver)
- [ ] Ensure focus indicators are visible
- [ ] Check `prefers-reduced-motion` behavior

**Tools:**
- Chrome DevTools (Lighthouse)
- axe DevTools
- WebAIM Contrast Checker

---

## 🚀 Performance Optimization

### **Critical CSS:**

Extract above-the-fold CSS and inline it:

```php
// functions.php in child theme
add_action('wp_head', function() {
    echo '<style id="sragi-critical">';
    // Paste minimal reset + tokens here
    echo '</style>';
}, 1);
```

### **Defer Non-Critical:**

```php
add_filter('style_loader_tag', function($html, $handle) {
    if ($handle === 'sragi-css') {
        return str_replace("rel='stylesheet'", "rel='preload' as='style' onload=\"this.onload=null;this.rel='stylesheet'\"", $html);
    }
    return $html;
}, 10, 2);
```

---

## 🐛 Troubleshooting

### **Issue: Links are blue, not black**

**Fix:** Ensure Bricks Theme Styles doesn't override link colors.

Go to: **Bricks → Theme Styles → Links**

Set:
```yaml
Link Color: inherit (or var(--text))
Link Hover: var(--link)
```

### **Issue: Fonts don't load**

**Check:**
1. Is child theme activated?
2. Is `sragi.css` enqueued in `functions.php`?
3. Clear browser cache + WordPress cache

### **Issue: Spacing looks wrong on mobile**

**Fix:** Ensure Bricks sections don't have inline padding overrides.

Remove inline styles from Bricks UI and let CSS handle it.

---

## 🔄 Update Workflow

When updating SRAGI CSS:

1. Update `sragi.css` in child theme
2. Bump version in `functions.php`:
   ```php
   wp_enqueue_style('sragi-css', ..., '2.1');  // ← Increment
   ```
3. Clear cache:
   - Browser (Ctrl + Shift + R)
   - WordPress (if using caching plugin)
   - Bricks (regenerate CSS in settings)

---

## 📚 Resources

- [Bricks Academy](https://academy.bricksbuilder.io/)
- [CSS Custom Properties (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)
- [SRAGI Documentation](https://sragi.org/docs)

---

## 🌿 Next Level: v2.1 Roadmap

**Planned Features:**
1. **Kairos Grid** - Organic, non-symmetrical layout system
2. **Typography Layer** - Google Fonts integration (Libre Baskerville, PT Serif)
3. **YAML Token Export** - Auto-generate `:root` from `SRAGI-BRAND-COLORS.yaml`
4. **Dark Mode Toggle** - User preference switcher
5. **Print Stylesheet** - Academic paper-ready formatting

---

**© 2025 Rune Solberg / Neptunia Media AS**
Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
See SRL-LICENSE.yaml for current version and details.

---

**File:** `/docs/implementation/SRAGI-CSS-BRICKS-GUIDE.md`  
**Maintainer:** Rune Solberg  
**Version:** 2.0  
**Last Updated:** October 29, 2025
