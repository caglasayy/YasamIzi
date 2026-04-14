## 2024-04-14 - Flutter Web Accessibility Basics
**Learning:** Flutter Web applications mount directly into an almost empty `index.html`. This means standard accessibility features, like screen reader language targeting, require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback in `frontend/web/index.html`.
**Action:** Always ensure the host `index.html` file includes proper `lang` attributes and `<noscript>` tags for Flutter Web projects.
