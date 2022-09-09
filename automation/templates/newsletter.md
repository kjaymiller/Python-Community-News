## Topics
{% for issue in issues %}
### {{issue.metadata.title}}

<small>Submitted by: [{{issue.metadata.user.login}}]({{issue.metadata.user.url}}) on {{issue.metadata.created_at}}</small>

{{issue.body.summary}}
{% endfor %}

## Upcoming Events
### CFPs

{% for cfp in cfps %}
* [{{cfp.body.conference_name}}]({{cfp.body.url}})] (Ends: {{cfp.body.cfp_dates}})
{% endfor %}

### Conferences

{% for conf in conferences %}
* [{{conf.body.conference_name}}]({{conf.body.url}})] - {{conf.conference_dates}}
{% endfor %}


### Watch the VOD on Youtube:
https://youtube.com/watch/{{youtube}}

### Take the content on the road with you!
https://transistor.fm/s/{{podcast}}
