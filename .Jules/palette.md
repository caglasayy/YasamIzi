## 2024-05-14 - Flutter Web Accessibility Defaults
**Learning:** Flutter web applications mount directly into an almost empty index.html. Standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback in `frontend/web/index.html`.
**Action:** Always check the `index.html` file of Flutter web apps for proper language attributes and JS fallbacks.
