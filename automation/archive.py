"""Takes Issues Filed in the last week and puts them in a file for the upcoming stream"""
import os
import pathlib
from datetime import datetime, timedelta

from jinja2 import Environment, FileSystemLoader

from engine import engine
from issues import get_issues_from_github

# Get the date of the next friday


def create_post(*, filename: str | pathlib.Path, template: str, **metadata) -> int:
    """Creates a markdown document for this week for render_engine to process"""
    filename = pathlib.Path("app/content").joinpath(pathlib.Path(filename))
    template = engine.get_template(template)
    return filename.write_text(template.render(metadata))


def get_show_file(directory: pathlib.Path, date: datetime.datetime) -> pathlib.Path:
    """Get the file for a show on a given date"""
    show_date = date.strftime("%Y-%m-%d")
    show_file = pathlib.Path(directory).joinpath(show_date).with_suffix(".md")
    return show_file