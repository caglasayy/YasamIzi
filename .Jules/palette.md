## 2026-05-18 - Base HTML Accessibility for Flutter Web
**Learning:** Flutter Web applications mount into an empty HTML file. Screen readers need `lang="tr"` on the `<html>` tag to correctly pronounce the Turkish interface, and a `<noscript>` tag is necessary to provide an accessible fallback for users with JavaScript disabled.
**Action:** Added `lang="tr"` to `<html>` and a localized `<noscript>` tag to `frontend/web/index.html`.
