"""Takes Issues Filed in the last week and puts them in a file for the upcoming stream"""
import os
from venv import create
import httpx
from datetime import datetime, timedelta
import pathlib
from jinja2 import FileSystemLoader, Environment
# Get the date of the next friday

api_key: str = os.environ.get('GITHUB_API_KEY', None)

loader = FileSystemLoader("./app/templates")
environment = Environment(loader=loader)

def get_last_friday():
    """Returns the previous friday"""
    upcoming_friday = datetime.today() - timedelta(4 - datetime.today().weekday())
    last_friday = upcoming_friday - timedelta(days=7)
    return last_friday.isoformat()
    
def get_issues_from_github():
    """Returns the issues filed in the last week"""
    url = 'https://api.github.com/repos/kjaymiller/Python-Community-News/issues'
    since_date = get_last_friday()
    params = {
        "query": "label=Content",
        "since": since_date
    }
    request = httpx.get(url, params=params)
    return request.json()

def create_post_for_week():
    """Creates a markdown document for this week for render_engine to process"""
    friday = (datetime.today() - timedelta(4 - datetime.today().weekday())).strftime("%Y-%m-%d")
    current_week = pathlib.Path('app/content').joinpath(friday).with_suffix('.md')
    issues = get_issues_from_github()
    template = environment.get_template("content_gen/episode_template.md")
    return current_week.write_text(template.render(issues=issues, date=friday))

if __name__ == "__main__":
    print(create_post_for_week())