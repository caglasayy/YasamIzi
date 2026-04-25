## 2026-04-25 - Flutter Web Base HTML Accessibility
**Learning:** Because Flutter web mounts directly into `index.html`, standard global accessibility aspects like screen reader language targeting and JavaScript fallbacks aren't handled by the framework components themselves. They must be explicitly set in the root `web/index.html`.
**Action:** When working on Flutter Web, always ensure `web/index.html` has proper language targeting (`lang` attribute on `<html>`) and robust `<noscript>` fallbacks for when the framework fails to load.
