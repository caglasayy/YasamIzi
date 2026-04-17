## 2024-04-17 - HTML Accessibility and Fallbacks in Flutter Web
**Learning:** Flutter Web applications mount into an almost empty index.html, which means standard accessibility features like screen reader language targeting (`<html lang="tr">`) and JS-disabled fallbacks (`<noscript>`) must be manually added to the root HTML file.
**Action:** Always verify the root index.html of Flutter Web projects contains the appropriate `lang` attribute and a styled `<noscript>` fallback for a complete baseline accessibility experience.
