# Theme Configuration

## Base theme recommendation

**Primary: Astra.** Lightweight (<50 KB), deep WooCommerce + Elementor
integration, native header/footer builder, per-page layout controls, and a
large library of starter templates. Best balance of speed and flexibility for
a large catalog store.

| Theme | Pros | Cons | Verdict |
|---|---|---|---|
| **Astra** (recommended) | Very fast, WooCommerce + Elementor friendly, granular controls, free | Some layout controls need Astra Pro | **Use this** as the parent. |
| **Hello Elementor** | Barest, fastest base; ideal if building 100% in Elementor Pro Theme Builder | Almost no styling out of the box; needs Elementor Pro to be practical | Good if you own Elementor Pro and want full control. |
| **Storefront** | Official WooCommerce theme, rock-solid commerce defaults | Heavier to customize, less Elementor-friendly, dated look | Fine for a pure-WooCommerce build without heavy Elementor use. |

This repo's child theme (`theme/`) targets **Astra** (`Template: astra`).

## Child theme setup

**Why a child theme:** it lets you customize styles/functions without editing
Astra directly, so Astra updates never overwrite your work.

**How it maps to this repo:**
- `theme/style.css` - theme header (`Template: astra`) + design tokens
  (CSS custom properties) + WooCommerce/pharmacy styles + light/dark mode.
- `theme/functions.php` - enqueues parent + child styles and Google Fonts,
  declares WooCommerce support, forces the INR symbol, sets products-per-page,
  adds a product trust badge and the dark-mode toggle.
- `theme/woocommerce/product-searchform.php` - a WooCommerce template override.

**Install:**
1. Install + activate **Astra** (Appearance > Themes > Add New).
2. Zip the `theme/` folder as `janaushadhi-child.zip` with `style.css` at the
   zip root, **or** copy it to `wp-content/themes/janaushadhi-child/`.
3. Appearance > Themes > Add New > Upload Theme > install > **Activate**
   "Jan Aushadhi Child".

## Color palette (pharmacy / healthcare)

Trust-forward medical greens and clinical blues on clean neutrals. Values are
defined as CSS variables in `theme/style.css` (`:root`).

| Token | Hex (light) | Use |
|---|---|---|
| Primary (green) | `#1B7A43` | Buttons, primary actions, price accents |
| Primary dark | `#146034` | Button hover, price text |
| Primary light | `#2E9E5B` | Highlights, success |
| Secondary (blue) | `#0F6FB8` | Links, secondary CTAs, focus outline |
| Secondary dark | `#0B568F` | Secondary hover |
| Accent | `#F5A623` | Sale badges, cart count, star ratings |
| Success | `#2E9E5B` | Success states |
| Warning | `#E8A100` | Warnings |
| Danger | `#C0392B` | Errors |
| Text | `#1A2B22` | Body text (AA on white) |
| Text muted | `#52605A` | Secondary text |
| Background | `#FFFFFF` | Page background |
| Background alt | `#F4F8F6` | Alternating sections, chips |
| Border | `#E2E8E5` | Card/input borders |

**Accessibility:** primary green `#1B7A43` and text `#1A2B22` both exceed WCAG
AA contrast (>=4.5:1) on white; the blue link `#0F6FB8` passes AA for normal
text. Focus states use a 3px blue outline. Keep white text on the green/blue
buttons (both pass AA for button text).

## Typography

- **Headings:** Poppins (500/600/700) - friendly, modern, trustworthy.
- **Body:** Inter (400/500/600) - highly legible at small sizes, great for
  dense product/medical text.
- Loaded via Google Fonts in `functions.php` with `display=swap`
  (for best performance, self-host the fonts - see `docs/performance.md`).
- **Scale:** base 16px (15px on small phones), body line-height 1.65, heading
  line-height 1.25. Suggested type scale: H1 ~2.2rem, H2 ~1.75rem, H3 ~1.4rem,
  body 1rem, small 0.85rem.

## Mobile responsive notes

- **Mobile-first:** most Indian pharmacy traffic is mobile; design and QA on
  phones first.
- **Breakpoints** (Astra/Elementor defaults): mobile <=544px, tablet <=921px,
  desktop above.
- **Sticky header + cart:** header uses `.ja-sticky-header`; keep the search
  bar and cart reachable on scroll.
- **Tap targets:** buttons enforce `min-height: 44px` on mobile.
- **Product grid:** collapses to 1 column at <=544px, 2 columns on small
  tablets. Set Elementor/WooCommerce columns per breakpoint.
- **Mobile menu:** Astra hamburger; keep primary links (Shop, Categories,
  Account, Cart) short.
- **Images:** lazy-load and serve scaled sizes (see performance doc).

## Dark mode approach

The child theme uses **CSS custom properties** as the single source of truth:
- `:root` defines the **light** palette.
- `@media (prefers-color-scheme: dark)` overrides the variables, so users with
  OS dark mode get dark automatically.
- `:root[data-theme="dark"]` allows an explicit manual override.
- A small **dependency-free toggle** (in `functions.php`) flips
  `data-theme` on `<html>` and stores the choice in `localStorage`.

Because every color references a variable, dark mode needs no per-component
rules. To use a plugin instead (e.g. "WP Dark Mode"), remove the
`janaushadhi_dark_mode_toggle` function and keep the variables. Dark palette:
near-black green-tinted background `#0E1512`, surfaces `#16221C`, brightened
primary `#37B36A`, links `#5FB0E8`, text `#E7EFEA`.
