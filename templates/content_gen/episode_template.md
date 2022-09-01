---
title: Weekly Community News - {{date}}
date: {{date}}
tags: {{tags}}
github: https://github.com/kjaymiller/Python-Community-News/blob/main/app/content/{{date}}.md
---

{% for issue in issues %}
# {{issue.title}}

<small>Submitted by: [{{issue.user.login}}]({{issue.user.url}}) on {{issue.created_at}}</small>

{{issue.body}}

{% endfor %}
