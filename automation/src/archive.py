"""Takes Issues Filed in the last week and puts them in a file for the upcoming stream"""
import pathlib
from datetime import datetime

from automation.engine import engine

# Get the date of the next friday


def create_post(*, filename: str | pathlib.Path, template: str, **metadata) -> int:
    """Creates a markdown document for this week for render_engine to process"""
    filename = pathlib.Path("app/content").joinpath(pathlib.Path(filename))
    jinja_template = engine.get_template(template)
    return filename.write_text(jinja_template.render(metadata))


def get_show_file(directory: pathlib.Path, date: datetime) -> pathlib.Path:
    """Get the file for a show on a given date"""
    show_date = date.strftime("%Y-%m-%d")
    show_file = pathlib.Path(directory).joinpath(show_date).with_suffix(".md")
    return show_file
