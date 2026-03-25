## 2023-10-24 - Accessibility Foundation for Flutter Web
**Learning:** Flutter Web applications mount into an almost empty `index.html`. Since the entire UI is drawn on a canvas or DOM nodes later, the initial HTML wrapper lacks structural accessibility context. Screen readers might fail to detect the application language or title correctly before JS fully initializes.
**Action:** Always ensure the entry `index.html` for Flutter Web apps has `lang="tr"` on the `<html>` tag, an accurate localized `<title>`, and a `<noscript>` fallback message for users with JavaScript disabled.
