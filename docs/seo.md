# SEO Configuration (Rank Math)

SEO runbook for the Jan Aushadhi WooCommerce store. Plugin: **Rank Math**.
Domain examples use `janaushadhi.example.com` - replace with the live domain.

## 1. Setup wizard
- **Rank Math > Setup Wizard**.
- Mode: **Advanced** (exposes schema + sitemap controls).
- Connect a free Rank Math account (optional but enables Content AI / analytics).
- Site type: **Online store / eCommerce**; enter the business name
  "Jan Aushadhi", logo, and a default social share image.
- Let Rank Math detect and enable the **WooCommerce** module.

## 2. Site-wide settings
- **Titles & Meta > Global Meta:** separator `-`; robots default
  `index, follow`.
- **Title format:** posts/pages `%title% %sep% %sitename%`.
- **Homepage:**
  - Title: `Jan Aushadhi Generic Medicines - Affordable, Genuine, Govt-Backed`
  - Description: `Buy quality generic medicines online at up to 50-90% less than
    branded prices. Government-backed PMBJP catalog, genuine medicines,
    fast delivery across India.`
- **Open Graph / Twitter:** set default OG image (1200x630), Twitter card =
  `summary_large_image`, OG type `website`.

## 3. Sitemaps
- **Rank Math > Sitemap Settings:** enable the XML sitemap.
- Include post types: **Products**, Pages, Posts.
- Include taxonomies: **Product categories** (`product_cat`); exclude tags if unused.
- Exclude: cart, checkout, my-account, thank-you (set them `noindex` too).
- Sitemap index URL: `https://janaushadhi.example.com/sitemap_index.xml`.
- Submit that URL in **Google Search Console** and **Bing Webmaster Tools**.

## 4. Meta / robots
- Default `index, follow` for products and product categories.
- **noindex** cart, checkout, my-account, order-received/thank-you, and internal
  search results (`?s=`). Set per-page in the Rank Math meta box or via
  Titles & Meta.
- Canonicals: Rank Math sets self-referencing canonicals automatically; for
  filtered/paginated shop URLs, ensure canonical points to the clean archive.

## 5. Schema / structured data
Rank Math + WooCommerce output structured data automatically; verify with the
Rich Results Test.

- **Product schema** (per product, automatic via WooCommerce integration):
  `name`, `sku` (Drug Code), `offers.price` (MRP), `offers.priceCurrency` = `INR`,
  `offers.availability` = `InStock`, `brand` = `Jan Aushadhi`.
- **AggregateRating / Review:** emitted from WooCommerce native reviews once
  products have ratings (`ratingValue`, `reviewCount`).
- **Organization / LocalBusiness (Pharmacy):**
  set in **Titles & Meta > Local SEO**:
  - `@type`: `Pharmacy`
  - name: `Jan Aushadhi`, logo, URL
  - address: full India store address
  - telephone: helpline number
  - openingHours: e.g. `Mo-Su 09:00-21:00`
  - `priceRange`: `Rs`
- **Breadcrumb schema:** enabled with breadcrumbs (below).
- **FAQ schema:** on the FAQ page, add Rank Math's **FAQ block** (Gutenberg) or
  mark the accordion Q&A as FAQ schema so Google can show rich FAQ results.

## 6. Breadcrumbs
- **Rank Math > General Settings > Breadcrumbs:** enable.
- Show breadcrumbs on products and archives; format
  `Home > Medicines > <Category> > <Product>`.
- If the theme doesn't auto-render them, add
  `[rank_math_breadcrumb]` (shortcode) or the PHP function to the product
  template / an Elementor shortcode widget.

## 7. Local SEO
- Complete **Local SEO** (Pharmacy) as above.
- Create/claim a **Google Business Profile** for the Kendra, matching NAP
  (Name, Address, Phone) exactly with the site.

## 8. Content SEO
- Give each of the 62 categories a unique meta title + description, e.g.
  Cardiovascular: `Affordable Generic Cardiovascular Medicines Online | Jan Aushadhi`.
- Use category focus keywords like "generic <category> medicines India",
  "affordable <drug> generic".
- Add **image alt text** to product/placeholder images (product name + "generic
  medicine").
- Keep product descriptions unique (the import already generates descriptive,
  non-duplicate copy per product).

## 9. Analytics
- Connect **Google Search Console** (verify via Rank Math or DNS).
- Add **GA4** (Rank Math Analytics module, Site Kit, or GA4 tag) - respect the
  cookie-consent banner.

## 10. Pre-launch SEO checklist
- [ ] Permalinks = Post name.
- [ ] Sitemap live at `/sitemap_index.xml` and submitted to GSC + Bing.
- [ ] Homepage + all 62 category pages have unique titles/descriptions.
- [ ] cart/checkout/account/search set to `noindex`.
- [ ] Product schema validates (Rich Results Test).
- [ ] LocalBusiness/Pharmacy schema present with correct NAP.
- [ ] FAQ schema on FAQ page.
- [ ] Breadcrumbs render + validate.
- [ ] GA4 + Search Console connected.
- [ ] Social OG image + defaults set.
- [ ] robots.txt not blocking products/media; HTTPS canonical.
