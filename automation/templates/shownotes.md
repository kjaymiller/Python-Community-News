
This week:
{% for issue in issues %}
- {{issue.title}}
{% endfor %}

{% for issue in issues %}
{% if 'url' in issue %}
{{issue.title}} - {{issue.url}}
{% endif %}
{% endfor %}

Podcast Episode at:
<REPLACE WITH PODCAST URL>

Newsletter Article at:
<REPLACE WITH NEWSLETTER URL>

Python Community News is a non-pippable look at the week in the Python community. Learn about conference announcements and the latest news around the Language you love.

Follow the hosts:
Jay (@kjaymiller) - https://twitter.com/kjaymiller
Jon (@jonafato) - https://twitter.com/jonafato

Chapters:
{% for issue in issues %}
{{issue.title}}: 00:00
{% endfor %}
