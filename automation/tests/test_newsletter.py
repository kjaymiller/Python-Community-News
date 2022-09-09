import datetime
import json
import pathlib
from tkinter import W

from automation.engine import engine
import httpx
import pytest
from automation.newsletter import (
    build_email_from_content,
    get_publish_time,
    schedule_email_from_post,
)


def test_shownotes_date_creation(date, time):
    """Given a date and time, return the publish time for the email in datetime format"""
    assert get_publish_time(date, time) == datetime.datetime.combine(date, time)


def test_shownotes_content(shownotes_text, newsletter_body, tmp_path):
    """Given the shownotes_text, return the body of the email"""
    filepath = tmp_path / pathlib.Path("test_path.md")
    filepath.write_text(shownotes_text)
    assert build_email_from_content(filepath) == newsletter_body


def test_shownotes_request_from_file(
    httpx_mock,
    newsletter_body,
    date,
    time,
):
    publish_date = datetime.datetime.combine(date, time)
    httpx_mock.add_response()
    publish_date = datetime.datetime.combine(date, time)

    with httpx.Client() as _:
        request = schedule_email_from_post(newsletter_body, publish_date=publish_date)
        content = bytes.decode(httpx_mock.get_requests()[0]._content, "utf-8")
        assert json.loads(content) == newsletter_body


def test_newsletter_template_exists():
    assert "newsletter.md" in engine.engine.list_templates()
