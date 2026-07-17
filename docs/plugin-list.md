# Plugin List

Plugins for the Jan Aushadhi WooCommerce store. Install **Required** first,
then **Recommended**. Payment/API keys are always entered in WP admin and
never committed to git.

## Required + Recommended

| Plugin | Type | Purpose | Notes |
|---|---|---|---|
| **WooCommerce** | Required | Core store engine: products, cart, checkout, orders, coupons, reviews | Free. Run its setup wizard (India / INR). Native product reviews + star ratings and coupons are built in - no extra plugin needed. |
| **Elementor** | Required | Drag-and-drop page builder for homepage + About/Contact/FAQ | Free tier is enough for the documented layout. |
| **Elementor Pro** | Optional | Theme Builder (custom header/footer/product templates), advanced widgets, forms | Paid. Nice-to-have; the free tier + Astra covers the basics. |
| **Rank Math SEO** | Required | SEO titles/meta, XML sitemaps, product & LocalBusiness schema, breadcrumbs | Free tier covers everything in `docs/seo.md`. |
| **Razorpay for WooCommerce** | Required | India payment gateway (cards, UPI, netbanking, wallets) | Free plugin. Keys entered in WP admin only. See `docs/woocommerce-settings.md`. |
| **TI WooCommerce Wishlist** | Required | Customer wishlists / "save for later" | Free. Alternative: **YITH WooCommerce Wishlist** (free + paid tiers). Recommend TI (fully free, no cap). |
| **WooCommerce PDF Invoices & Packing Slips** | Required | Auto-attach PDF invoices to order emails; packing slips | Free. |
| **LiteSpeed Cache** | Required (host-dependent) | Full-page cache, object cache, CSS/JS optimize, image WebP, CDN | Free. **Use only if the host runs LiteSpeed/OpenLiteSpeed.** Otherwise use W3 Total Cache. |
| **W3 Total Cache** | Required (alternative) | Page/object/browser cache, minify | Free. Use when the host is **not** LiteSpeed (Apache/Nginx). Pick one caching plugin, not both. |
| **ShortPixel Image Optimizer** | Recommended | Bulk compress + WebP/AVIF for a large image library | Freemium (monthly credit; paid for bulk). Best for a 2,400+ product catalog. |
| **Smush** | Recommended (alternative) | Free image compression + lazy load | Free tier is generous; simpler than ShortPixel. Use one image optimizer. |
| **Cloudflare** | Required | CDN, DNS proxy, edge cache, APO for WordPress, security | Free plan works; APO is a small paid add-on. See `docs/performance.md`. |
| **Wordfence Security** | Recommended | Firewall, malware scan, login protection | Free tier solid; important for a store handling customer/payment data. |
| **UpdraftPlus** | Recommended | Scheduled backups to remote storage (Drive/S3) | Free tier covers scheduled backups. |
| **Contact Form 7** or **WPForms Lite** | Recommended | Contact page form, enquiries | Both free. WPForms is more beginner-friendly; CF7 is lightweight. |
| **Cookie/consent plugin** (e.g. CookieYes) | Recommended | Cookie consent / privacy compliance banner | Free tier available; good practice for an India ecommerce site. |
| **FiboSearch (Ajax Search for WooCommerce)** | Recommended | Fast live product search for a large catalog | Free tier; greatly improves search UX across 2,439 products. |

## Coupons / marketing (no plugin required)
WooCommerce core includes **coupons**. Enable at
**WooCommerce > Settings > General > Enable coupons**, then create them at
**Marketing > Coupons** (percentage / fixed cart / fixed product, usage limits,
expiry, category restrictions). No paid coupon plugin is needed for standard
discounts.

## Free vs paid summary
- **Fully free (all features used here):** WooCommerce, Elementor (free),
  Rank Math (free), Razorpay for WooCommerce, TI Wishlist, PDF Invoices,
  LiteSpeed Cache / W3 Total Cache, Smush (free), Wordfence (free),
  UpdraftPlus (free), Contact Form 7 / WPForms Lite, CookieYes (free),
  FiboSearch (free).
- **Paid / freemium (optional):** Elementor Pro, ShortPixel bulk credits,
  Cloudflare APO, YITH Wishlist premium.

## Install order
1. WooCommerce (run wizard) 2. Elementor (+ Pro) 3. Rank Math 4. Razorpay
5. TI Wishlist 6. PDF Invoices 7. Caching plugin (LiteSpeed **or** W3TC)
8. Image optimizer (ShortPixel **or** Smush) 9. Cloudflare 10. FiboSearch
11. Security/backup/forms/consent.

Install caching and Cloudflare **last**, after the site content and catalog
are in place, so you can flush and validate cache against the finished site.

## Count summary
- **Required:** 8 (WooCommerce, Elementor, Rank Math, Razorpay, TI Wishlist,
  PDF Invoices, one caching plugin, Cloudflare).
- **Recommended:** 7 (ShortPixel/Smush image optimizer, Wordfence, UpdraftPlus,
  Contact form, consent, FiboSearch, plus Elementor Pro as optional upgrade).
- **Total documented:** 15 distinct plugins (choosing one of each either/or pair:
  caching LiteSpeed-or-W3TC, image ShortPixel-or-Smush, form CF7-or-WPForms).
