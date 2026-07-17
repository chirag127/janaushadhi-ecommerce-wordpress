# Homepage Layout (Elementor)

Section-by-section build spec for the Jan Aushadhi homepage in Elementor, plus
notes for About / Contact / FAQ pages. Build with Astra + Elementor (free tier
is sufficient; Elementor Pro's Theme Builder is optional for header/footer).

Palette references the child-theme tokens (green `#1B7A43`, blue `#0F6FB8`,
accent `#F5A623`). After building, set this page as the homepage under
**Settings > Reading > A static page**.

---

## 1. Announcement / top bar
- **Purpose:** push the free-shipping offer + helpline.
- **Widgets:** Elementor "Text Editor" or a thin section with two columns; or
  Astra's top bar.
- **Content:** left "Free delivery on orders over Rs 500" | right
  "Helpline: 1800-XXX-XXXX (9am-9pm)" (use `[ja_helpline]` shortcode).
- **Layout:** full-width, small green (`#1B7A43`) bar, white text.

## 2. Header
- **Purpose:** navigation, search, cart, account - always reachable.
- **Widgets:** Astra header (or Elementor Pro Header). Site logo + Nav Menu +
  WooCommerce **Menu Cart** + a search field + account/wishlist icons.
- **Content:** logo (left); menu: **Home, Shop, Categories, About, Contact,
  FAQ**; prominent **product search bar** (uses the branded
  `product-searchform.php` / FiboSearch); **cart** icon with `.ja-cart-count`;
  **wishlist** icon (TI Wishlist); **My Account**.
- **Layout:** sticky on scroll (`.ja-sticky-header`); collapses to hamburger on
  mobile with search + cart still visible.

## 3. Hero banner
- **Purpose:** headline value prop + primary CTA + trust signal.
- **Widgets:** Section with background image/overlay; Heading + Text + Button +
  a `.ja-trust-badge`.
- **Content:**
  - H1: "Genuine Generic Medicines - up to 50-90% Cheaper"
  - Sub: "Government-backed PMBJP quality medicines, delivered across India."
  - CTA button: **"Shop Medicines"** -> Shop page (green primary button).
  - Trust badge: "Govt. of India | PMBJP" chip.
- **Layout:** full-width, 2 columns desktop (copy left, hero image right),
  stacked on mobile; overlay for text contrast (WCAG AA).

## 4. Search bar (prominent)
- **Purpose:** let visitors search 2,439 products immediately.
- **Widgets:** WooCommerce **Product Search** widget or FiboSearch shortcode in
  a centered section.
- **Content:** placeholder "Search medicines by name...".
- **Layout:** centered, max-width ~700px, pill input (`.ja-search-form`). If the
  header already has a strong search, make this a slim reinforcing band.

## 5. Category grid
- **Purpose:** route shoppers into the main therapeutic categories.
- **Widgets:** Elementor Icon Box grid (or "Product Categories" widget).
- **Content:** 8-12 key categories with icons linking to their archives:
  Cardiovascular (CVS), Anti-Diabetic, Antibiotics, Central Nervous System (CNS),
  Respiratory, Gastrointestinal (GIT), Analgesic/Anti-Inflammatory,
  Supplement/Vitamin/Mineral, Dermatology, Surgical & Medical Consumables +
  a "View all categories" link.
- **Layout:** responsive grid 4-up desktop / 2-up mobile; cards use
  `.ja-card` styling.

## 6. Featured products
- **Purpose:** surface popular / featured medicines.
- **Widgets:** WooCommerce **Products** widget (or Elementor Pro Loop).
- **Content:** 8 featured/best-selling products (mark some "Is featured?" in
  WooCommerce). Show price, add-to-cart, wishlist icon, star rating.
- **Layout:** 4 columns desktop, 2 mobile; "View all" -> Shop.

## 7. Trust / why-choose-us
- **Purpose:** build confidence for buying medicines online.
- **Widgets:** Icon Box row (3-4 items).
- **Content:** "WHO-GMP certified quality", "Government-backed PMBJP",
  "Genuine generics - same salt, lower price", "Assured quality & safety".
- **Layout:** `.ja-section--alt` background, 4 columns desktop / 2 mobile,
  green/blue icons.

## 8. How it works
- **Purpose:** reduce ordering friction.
- **Widgets:** numbered Icon Box / steps.
- **Content:** 1) Search or browse -> 2) Add to cart -> 3) Checkout (Razorpay/COD)
  -> 4) Fast delivery.
- **Layout:** 4-step horizontal row, stacks on mobile.

## 9. Testimonials (optional)
- **Widgets:** Testimonial Carousel.
- **Content:** 3-5 short customer quotes about savings/reliability.
- **Layout:** carousel, 1-2 visible.

## 10. Newsletter / helpline CTA
- **Purpose:** capture leads + reassure with human support.
- **Widgets:** a form (WPForms/CF7) + heading; or a call-out with the helpline.
- **Content:** "Get offers & health tips" email signup, and "Questions? Call
  1800-XXX-XXXX".
- **Layout:** full-width green band, white text, single input + button.

## 11. Footer
- **Purpose:** navigation, trust, legal, contact.
- **Widgets:** multi-column footer (Astra footer or Elementor Pro Footer).
- **Columns:**
  1. **About Jan Aushadhi** - short blurb + logo.
  2. **Quick links** - Shop, About, Contact, FAQ, Track Order (My Account),
     Privacy, Terms, Refund policy.
  3. **Top categories** - CVS, Anti-Diabetic, Antibiotics, CNS, Respiratory.
  4. **Contact** - address, helpline, email, hours; **payment icons**
     (Razorpay/UPI/cards); social links.
- **Bottom bar:** copyright "(c) Jan Aushadhi" + "Powered by PMBJP".

---

## Content-page layout notes

### About Us
- **Widgets:** Heading + Text + Image + Icon Boxes + stats counters.
- **Content:** the PMBJP mission (affordable quality generics), what Jan Aushadhi
  is, quality assurance (WHO-GMP), reach/impact stats, and a CTA to Shop.
- **Layout:** hero heading, alternating text/image rows, a stats band,
  closing CTA.

### Contact
- **Widgets:** contact form (**WPForms** or **Contact Form 7**), Google **Map**
  embed, Icon List for address/phone/email/hours.
- **Content:** enquiry form (name, email, phone, message), Kendra address, map,
  helpline, support hours.
- **Layout:** 2 columns desktop (form left, details+map right), stacked mobile.

### FAQ
- **Widgets:** Elementor **Accordion** (or Rank Math **FAQ block** so it emits
  FAQ schema - see `docs/seo.md`).
- **Content:** Q&As - "Are generic medicines safe/effective?", "How much can I
  save?", "What payment methods?", "Delivery time & areas", "Do I need a
  prescription?", "Returns/refunds", "How do I track my order?".
- **Layout:** single-column accordion, grouped by topic; add FAQ schema for rich
  results.
