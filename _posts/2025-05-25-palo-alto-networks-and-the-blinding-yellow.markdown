---
layout: post
title: "Palo Alto Networks and the Blinding Yellow"
date: 2025-05-25 00:00:00 -0600
categories: blog
---
# Customizing the Palo Alto NGFW Login Screen with "Login That Blinded Me"

The default login page for Palo Alto Networks’ Next-Generation Firewall (NGFW) is visually aggressive. Its bright yellow background and low-contrast text elements can be jarring—especially in low-light environments. For users who regularly interact with the firewall’s web interface, this isn’t just an aesthetic concern; it’s a usability issue.

The **Login-That-Blinded-Me** project was created to solve that problem by providing a clean, readable, dark theme for the NGFW login and logout screens using standard CSS.

## Overview

This project is a single-file CSS stylesheet designed to be injected into the browser using a userstyle manager like [Stylus](https://add0n.com/stylus.html). It targets the login (`/php/login.php`) and logout (`/php/logout.php`) pages of Palo Alto NGFWs, overriding their default styling without requiring any changes to the device itself.

Because this is a client-side approach, it’s safe to use in environments where modifying the firewall firmware or internal files is prohibited or unsupported.

## What It Does

* **Applies a dark background**: Replaces the intense yellow with a muted dark gray, reducing eye strain.
* **Improves contrast**: Adjusts font colors and input field styles to improve legibility.
* **Redesigns form layout**: Minor alignment and spacing improvements make the UI easier to scan and interact with.
* **Cleans up unused visual noise**: Elements that were purely decorative or distracting have been toned down or removed entirely.
* **Adds maintainability via variables**: CSS variables are used for colors, making it easy to adjust the theme to suit your preference.

## What It Doesn’t Do

* **No JavaScript injection**: This is a pure CSS solution, avoiding any risk of altering page behavior.
* **Doesn’t modify the firewall**: It’s important to note this runs entirely on the browser, via Stylus or a similar plugin.
* **No support for admin UI pages**: The style is scoped only to the login and logout pages. It does not alter the full WebGUI after authentication.

## Why Not Just Use a Browser Theme?

Generic dark mode browser extensions do a poor job with this particular interface because the PANW login screen uses hardcoded inline styles and non-standard layout practices. This stylesheet is tailored specifically for this use case and overrides these quirks with minimal assumptions about what firmware version you’re running.

## Installation Instructions

1. **Install Stylus**
   Add Stylus to your browser via the [Chrome Web Store](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne) or [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/styl-us/).

2. **Copy the CSS File**
   Get the `login-that-blinded-me.css` from the GitHub repo:
   [https://github.com/greaselovely/Login-That-Blinded-Me](https://github.com/greaselovely/Login-That-Blinded-Me)

3. **Add New Style in Stylus**
   In Stylus, create a new style, paste the contents of the CSS file

4. **Save and Enable**
   Save the style and make sure it’s active. Visit your firewall login page and verify the new style is applied.

## Use Cases

* Admins logging in frequently from laptops or desktops, especially in dimly lit NOCs.
* Power users who prefer visual consistency with dark-themed terminal and browser environments.
* Security engineers using NGFWs in environments with strict change controls who still want a more readable UI.

## Contribution and Licensing

This project is intentionally minimal. If you encounter layout changes in a future PAN-OS version or want to extend styling to other parts of the WebUI, pull requests are welcome.

The CSS is licensed under the MIT License. Use it freely in personal or professional environments.

---

You can find the full source and installation notes at:
[https://github.com/greaselovely/Login-That-Blinded-Me](https://github.com/greaselovely/Login-That-Blinded-Me)

---

Other Posts You May Want To Cover in Syrup:
