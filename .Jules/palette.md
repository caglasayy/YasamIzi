## 2024-05-24 - Flutter Web Initial Payload Accessibility
**Learning:** Flutter web applications mount into an almost empty index.html, which means standard web accessibility tools (like screen readers determining the document language via `lang` attribute) fail before the app fully loads. Additionally, a blank screen appears if JavaScript is disabled.
**Action:** Always ensure the entry `index.html` has explicit `lang` attributes matching the primary content language and includes styled `<noscript>` fallbacks to inform users about the JS requirement.
