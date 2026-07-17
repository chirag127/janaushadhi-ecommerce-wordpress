# Performance & CDN

Performance runbook for the Jan Aushadhi store (2,439-product catalog).
CDN: **Cloudflare**. Caching: **LiteSpeed Cache** (LiteSpeed hosts) or
**W3 Total Cache**. Images: **ShortPixel** or **Smush**.

## Goals (Core Web Vitals)
- **LCP** < 2.5 s
- **INP** < 200 ms
- **CLS** < 0.1
- Target **PageSpeed Insights** >= 90 mobile where feasible (>= 80 acceptable
  for WooCommerce), >= 95 desktop.

## 1. Cloudflare CDN
1. Add the site at cloudflare.com; update the domain's **nameservers** to the
   two Cloudflare nameservers.
2. In Cloudflare DNS, set the site records to **Proxied** (orange cloud).
3. **SSL/TLS:** mode **Full (strict)** (requires a valid origin certificate).
4. **Speed > Optimization:** enable **Brotli**; enable Auto Minify (JS/CSS/HTML)
   *only after testing* - it can conflict with Elementor; if layout breaks,
   turn CSS/JS minify off in Cloudflare and let the caching plugin minify instead.
5. **Caching > Configuration:** caching level **Standard**; Browser Cache TTL
   >= 4 hours (static assets longer).
6. Install the **Cloudflare** WordPress plugin; enable **APO (Automatic Platform
   Optimization for WordPress)** to edge-cache HTML for logged-out users.
7. **Cache-bypass rules** (Rules > Page Rules or Cache Rules) for:
   `*/cart*`, `*/checkout*`, `*/my-account*`, `*/wp-admin*`, `*/wp-login*`,
   and any URL with WooCommerce cart cookies - set **Cache Level: Bypass**.
8. Keep **Rocket Loader off** (breaks Elementor/WooCommerce JS ordering).

## 2. Caching plugin
Pick **one** (never run two page-cache plugins):

**LiteSpeed Cache** (use on LiteSpeed/OpenLiteSpeed hosts - best option):
- Enable **Page Cache** and (if available) **Object Cache** (Redis/Memcached).
- **Cache > Excludes:** exclude cart, checkout, my-account and WooCommerce
  cart-fragment/AJAX URLs.
- **Page Optimization:** minify + combine CSS/JS, defer/async JS, lazy-load
  images/iframes, generate **Critical CSS**. Test Elementor pages after each
  toggle; disable "combine" if the layout breaks.
- Enable **image WebP** (LiteSpeed can optimize images itself - then you may skip
  a separate image plugin).
- **Database:** clean revisions, transients, spam.

**W3 Total Cache** (non-LiteSpeed Apache/Nginx hosts):
- Enable **Page Cache** (Disk: Enhanced) and **Browser Cache**.
- Enable **Object Cache** only with Redis/Memcached available.
- **Minify:** enable cautiously (manual mode for Elementor); test thoroughly.
- Set the CDN section to work with Cloudflare (or rely on the Cloudflare plugin).

**WooCommerce cache safety (both plugins + Cloudflare):**
- Never cache cart/checkout/my-account.
- Exclude the `woocommerce_cart_hash`, `woocommerce_items_in_cart`, and session
  cookies from cache; keep **cart fragments (AJAX)** working so the cart count
  updates without a full-page cache serving stale HTML.

## 3. Image optimization
Critical for a large catalog once product images are added.
- **ShortPixel** (best for bulk) or **Smush** (free) - bulk-optimize the media
  library.
- Convert to **WebP/AVIF** and serve next-gen formats.
- **Lazy-load** below-the-fold images.
- Upload/serve **correctly sized** images; set featured-image and catalog
  thumbnail sizes in WooCommerce so the store never ships oversized files.
- Add a lightweight global placeholder image (products currently have no images).

## 4. Database & hosting
- **PHP 8.1+**, OPcache enabled.
- **MySQL/MariaDB** with adequate memory; use **Redis** object cache if the host
  offers it (big win for WooCommerce + a 2,439-product catalog).
- Real cron: set `DISABLE_WP_CRON` + a server cron for reliability.
- Hosting: a **managed WordPress host** or a **LiteSpeed VPS** (LiteSpeed +
  LSCache + QUIC.cloud is an excellent, cheap combo for India traffic).

## 5. Elementor performance
- Enable Elementor **Experiments:** improved CSS/asset loading, "Optimized
  DOM Output", and load font-awesome/eicons only when used.
- Reduce widgets per section; avoid heavy animations.
- **Self-host Google Fonts** (Elementor setting or a plugin) to cut third-party
  requests - overrides the CDN font load in the child theme.
- Minimize third-party scripts (chat widgets, trackers).

## 6. Catalog-scale notes (2,439 products)
- Keep shop/category pages **paginated** (24/page - set in the child theme).
- Use **FiboSearch** for fast AJAX product search instead of default WP search
  across thousands of rows.
- Avoid heavy homepage product queries; feature a small curated set, lazy-load
  the category grid.
- Enable object caching so category/term and product queries are cached.
- Consider pre-warming cache for top categories after deploys.

## 7. Pre-launch performance checklist
- [ ] Cloudflare proxied, SSL Full (strict), APO on, cache-bypass rules for
      cart/checkout/account.
- [ ] One caching plugin configured; cart/checkout/account excluded; cart
      fragments working.
- [ ] Images optimized + WebP + lazy-load; placeholder set.
- [ ] Fonts self-hosted; Elementor experiments on.
- [ ] PHP 8.1+, Redis object cache if available, real cron.
- [ ] LCP < 2.5s, INP < 200ms, CLS < 0.1 on a real product + category page.
- [ ] Tested with **PageSpeed Insights**, **GTmetrix**, **WebPageTest** on
      mobile + desktop after cache warm-up.
