---
title: Weekly Community News - {{date}}
date: {{date}}
tags: {{tags}}
youtube: {{youtube}}
podcast: {{podcast}}
github: https://github.com/kjaymiller/Python-Community-News/blob/main/app/content/{{date}}.md
---

## Topics
{% for issue in issues %}
### {{issue.title}}

<small>Submitted by: [{{issue.user.login}}]({{issue.user.url}}) on {{issue.created_at}}</small>

{{issue.body}}

{% endfor %}

## Open CFPs and Upcoming Conferences
### CFPs Open
{% for cfp in cfps %}
- [{{cfp.title}}]({{cfp.url}})
{% endfor %}

### Conferences
{% for conference in conferences %}
- [{{conference.title}}]({{conference.url}})
{% endfor %}