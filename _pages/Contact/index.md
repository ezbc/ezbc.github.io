---
layout: page
title:  "Contact"
permalink: "/contact"
---

{% assign socialLinkedin = site.social_networks | where: "name",  "linkedin" %}
{% assign socialGithub = site.social_networks | where: "name",  "github" %}

Feel free to reach out to me on [Linkedin]({{ socialLinkedin[0].url }}) or
peruse my [Github]({{ socialGithub[0].url }}) profile.
