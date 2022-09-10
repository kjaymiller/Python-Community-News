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
### [{{issue.metadata.title}}]({{issue.metadata.user.url}})

<small>Submitted by: [{{issue.metadata.user.login}}]({{issue.metadata.user.url}}) on {{issue.metadata.created_at}}</small>

{{issue.body.summary}}

{% endfor %}

## Open CFPs and Upcoming Conferences
### CFPs Open
{% for cfp in cfps %}
- [{{cfp.body.conference_name}}]({{cfp.body.url}})
{% endfor %}

### Conferences
{% for conference in conferences %}
- [{{conference.body.conference_name}}]({{conference.body.url}})
{% endfor %}
