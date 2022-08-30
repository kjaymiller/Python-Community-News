---
subject: Weekly Community News - {{date}}
github: https://github.com/kjaymiller/Python-Community-News/blob/main/app/content/{{date}}.md
youtube: {{youtube}}
podcast: {{podcast}}
---

## Topics
{% for issue in issues %}
### {{issue.title}}

<small>Submitted by: [{{issue.user.login}}]({{issue.user.url}}) on {{issue.created_at}}</small>

{{issue.body}}
{% endfor %}

### Watch the VOD on Youtube:
https://youtube.com/watch/{{youtube}}

### Take the content on the road with you!
https://transistor.fm/s/{{podcast}}