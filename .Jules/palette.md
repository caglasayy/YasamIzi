## 2024-05-24 - Flutter Web Accessibility Baseline
**Learning:** Flutter Web applications mount directly into an almost empty `index.html`. This means standard accessibility features like screen reader language targeting and fallback for users without JavaScript must be explicitly added to this HTML file, not just within the Dart/Flutter code.
**Action:** Always ensure `frontend/web/index.html` has an explicit `lang` attribute (e.g., `<html lang="tr">`) and a `<noscript>` tag for proper fallback experience.
