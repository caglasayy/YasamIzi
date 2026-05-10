## 2024-10-24 - Flutter Web Accessibility Defaults
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., <html lang="tr">) and <noscript> tags for fallback.
**Action:** Always check the main index.html for base web accessibility attributes before assuming the Flutter framework handles them.
