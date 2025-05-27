---
layout: post
title: "EDL and the Tool I Wrote For You"
date: 2025-05-27 00:00:00 -0600
categories: blog
---
KineticLull is a self-hosted web application written in Python that helps teams manage External Dynamic Lists (EDLs) in a structured and accessible way. These EDLs, lists of IPs, domains, or URLs, are commonly used by firewalls, proxies, and security tools to enforce blocking, filtering, or routing decisions. Instead of manually updating these lists across different systems or relying on external services, KineticLull provides a central interface for maintaining them, with support for both human interaction and API automation.

The application is designed to run on Linux systems, specifically tested with Ubuntu 20/22 and Fedora 39. It uses Python 3.12 and a lightweight Flask-based backend. Installation scripts are provided to set up Python, create a virtual environment, install dependencies, and configure the app. Once running, you access it via a browser, and the data is served locally, no cloud or external services involved unless you explicitly configure them.

KineticLull is especially useful for internal teams that want to manage allow/block lists without giving everyone direct access to the firewall or proxy. For example:

* A SOC analyst can add or suggest new entries to an EDL without logging into the firewall.
* A manager or team lead can review, approve, or reject proposed entries through a browser-based interface.
* An automation script can fetch threat intel feeds (like from AbuseIPDB or open-source blocklists), clean and transform the data, and push updates directly to a KineticLull EDL via its API.
* An IT team can clone, export, or archive EDLs as part of routine operations or change control processes.

The application supports access controls through ACLs, and you can assign different permissions to different EDLs. There's also support for documentation and comments so each EDL can include a rationale or operational context.

From an operational standpoint, this kind of tool is helpful when you need auditability, consistency, and separation of duties. You can delegate list management without giving full network access, and you can automate inputs without losing human oversight. It’s especially relevant in environments that use Palo Alto Networks firewalls, Squid proxies, or similar tools that support EDLs via HTTP(S) feeds.

Because it’s open source and runs entirely in your own environment, you have full control. You can adjust how the API works, add integrations with ticketing systems, or change how permissions are structured, all without depending on a third party.

GitHub repo: [https://github.com/greaselovely/KineticLull](https://github.com/greaselovely/KineticLull)
Docs and info: [http://kineticlull.com](http://kineticlull.com)

---

Other Posts You May Want To Cover in Syrup:
