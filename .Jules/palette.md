## 2026-04-21 - [Flutter Web Accessibility Basics]
**Learning:** Flutter Web applications mount into an empty index.html, meaning standard HTML accessibility features like screen reader language targeting and JS-disabled fallbacks are not provided out-of-the-box and must be explicitly added to the index.html wrapper.
**Action:** Always add `lang="tr"` to the `<html>` tag and a helpful `<noscript>` block for Flutter Web projects in this repository to ensure baseline accessibility.
