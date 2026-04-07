## 2024-05-14 - Flutter Web Accessibility Baseline
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting and graceful degradation (JavaScript disabled) are easily overlooked because the UI isn't built in HTML.
**Action:** Always verify the mounting `index.html` has `<html lang="...">` for screen readers and a `<noscript>` tag for fallback functionality, as these cannot be set dynamically by the Flutter application early enough for all user agents.
