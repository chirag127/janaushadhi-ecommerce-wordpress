# Jan Aushadhi Child Theme

Minimal child theme built on **Astra** for the Jan Aushadhi generic-medicines store.

## Files
- `style.css` - theme header + design tokens (CSS custom properties) + WooCommerce/pharmacy styles + light/dark mode.
- `functions.php` - enqueues parent+child styles and Google Fonts, declares WooCommerce support (gallery zoom/lightbox/slider), forces INR rupee symbol, sets 24 products/page, adds a product-page trust badge, `[ja_helpline]` shortcode, and a dependency-free dark-mode toggle.
- `woocommerce/product-searchform.php` - WooCommerce template override for a pharmacy-branded product search form.

## Install
1. Install and activate the **Astra** parent theme (Appearance > Themes > Add New > search "Astra").
2. Zip this `theme/` folder as `janaushadhi-child.zip` (the zip's top level must contain `style.css`), OR copy it to `wp-content/themes/janaushadhi-child/`.
3. Appearance > Themes > Add New > Upload Theme > choose the zip > Install > **Activate**.

## Adding more template overrides
Copy any file from `wp-content/plugins/woocommerce/templates/` into
`theme/woocommerce/<same-relative-path>` and edit. WooCommerce automatically
uses the theme copy. Keep overrides minimal and re-check them after major
WooCommerce updates.

## Dark mode
The child theme ships a small toggle button (bottom-right). It flips
`data-theme="dark"` on `<html>` and persists the choice in localStorage.
CSS variables in `style.css` do the theming and also honor
`prefers-color-scheme: dark` automatically. Remove the toggle in
`functions.php` (`janaushadhi_dark_mode_toggle`) if you prefer a plugin.
