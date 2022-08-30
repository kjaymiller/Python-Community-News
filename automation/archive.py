"""Takes Issues Filed in the last week and puts them in a file for the upcoming stream"""
import os
import pathlib
from datetime import datetime, timedelta
from issues import get_issues_from_github

import httpx
from jinja2 import Environment, FileSystemLoader

# Get the date of the next friday

api_key: str = os.environ.get("GITHUB_API_KEY", None)

loader = FileSystemLoader("./app/templates")
environment = Environment(loader=loader)


def get_last_friday():
    """Returns the previous friday"""
    upcoming_friday = datetime.today() - timedelta(4 - datetime.today().weekday())
    last_friday = upcoming_friday - timedelta(days=7)
    return last_friday.isoformat()


def create_post_for_week():
    """Creates a markdown document for this week for render_engine to process"""
    friday = (datetime.today() - timedelta(4 - datetime.today().weekday())).strftime(
        "%Y-%m-%d"
    )
    current_week = pathlib.Path("app/content").joinpath(friday).with_suffix(".md")
    issues = get_issues_from_github()
    template = environment.get_template("content_gen/archive.md")
    return current_week.write_text(template.render(issues=issues, date=friday))


if __name__ == "__main__":
    print(create_post_for_week())
