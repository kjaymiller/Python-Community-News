import datetime
import os
import pathlib
from typing import Generator

import frontmatter
import httpx

hour = str
minute = str
buttondown_api_key = os.getenv("BUTTONDOWN_API_KEY")
header = {"Authorization": f"Token {buttondown_api_key}"}

schedule_email_url = "https://api.buttondown.email/v1/scheduled-emails"


def get_publish_time(
    date: datetime.datetime,
    time: datetime.time,
) -> datetime.datetime:
    """Helper for getting the date and time for when to schedule the email"""
    return datetime.datetime.combine(date, time)


def build_email_from_content(
    filepath: pathlib.Path,
) -> dict[str, str]:
    """
    Uses frontmatter to get the subject and returns a partial of the body to be used to schedule the email.
    """
    content = frontmatter.load(filepath)
    subject = content.metadata.get("subject")
    body = {
        "email_type": "public",
        "body": content.content,
        "subject": subject,
    }
    return body


def schedule_email_from_post(
    body: dict[str, str],
    publish_date: datetime.datetime,
) -> httpx.Response:
    """
    Returns the status code of the request.
    The the `publish_date` time are required to schedule the email.
    """

    body.update({"publish_date": publish_date.isoformat()})
    request = httpx.post(
        schedule_email_url,
        headers=header,
        json=body,
    )
    return request
