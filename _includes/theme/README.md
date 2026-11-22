# Site theme

A small Jekyll theme that replaced Minimal Mistakes. It started as a close
visual match for MM's "default" skin; from here it's ours to change.

## Files

| File | Role |
|------|------|
| `_layouts/default.html` | HTML shell: head, masthead, footer, scripts |
| `_layouts/single.html` | Content page: optional left nav, title, optional TOC |
| `_includes/theme/head.html` | `<title>`, meta tags, stylesheet |
| `_includes/theme/masthead.html` | Top bar (site title + subtitle, optional `main:` links) |
| `_includes/theme/sidebar-nav.html` | Left nav from `_data/navigation.yml` |
| `_includes/theme/footer.html` | Footer links (`footer.links` in `_config.yml`) and copyright |
| `_sass/theme/_tokens.scss` | **Colors, fonts, widths, font-size steps. Start here.** |
| `_sass/theme/_base.scss` | Typography, links, lists, tables, code, math |
| `_sass/theme/_layout.scss` | Masthead, sidebar, content/TOC grid, footer |
| `_sass/theme/_syntax.scss` | Code highlighting (generated: `rougify style github --scope=.highlight`) |
| `assets/js/theme.js` | Mobile menu toggle, "On this page" TOC, wide inline math |

Site-specific hooks, kept outside the theme so it can be reused:

- `_includes/head/custom.html`: fonts, MathJax, notebook-link script
- `_includes/footer/custom.html`: Read the Docs ad placement
- `assets/css/main.scss`: imports the theme partials, then site-only styles

## Front matter the layouts understand

```yaml
layout: single          # default for pages (set in _config.yml)
title: "Page title"
sidebar:
  nav: "ml"             # key in _data/navigation.yml
toc: true               # "On this page" box built from h2/h3 headings
toc_label: "In this unit"
classes: [wide]         # TOC goes above the content, not in a side column
math: true              # load MathJax (handled in head/custom.html)
```

## Reusing it on another site (e.g. aet-cs)

Copy `_layouts/`, `_includes/theme/`, `_sass/theme/`, `assets/js/theme.js`,
and the `@import "theme/..."` lines from `assets/css/main.scss`. Create
your own `_includes/head/custom.html` and `_includes/footer/custom.html`
(they can be empty). Remove `theme:` / `remote_theme:` from that site's
`_config.yml`. Its pages keep working as long as they use `layout: single`
or `layout: default`; MM-only layouts like `home`, `archive`, `splash`, or
`posts` would need their own layout files.
