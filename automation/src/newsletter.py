import datetime
import os
from collections import namedtuple

import httpx

buttondown_api_key = os.getenv("BUTTONDOWN_API_KEY")
header = {"Authorization": f"Token {buttondown_api_key}"}

schedule_email_url: str = "https://api.buttondown.email/v1/scheduled-emails"
Shownotes = namedtuple("Shownotes", "subject content publish_date")


def build_email_from_content(
    shownotes: Shownotes,
) -> httpx.Response:
    """
    Parse the shownotes object to build the email
    """
    body = {
        "email_type": "public",
        "body": shownotes.content,
        "subject": shownotes.subject,
        "publish_date": shownotes.publish_date,
    }
    request = httpx.post(
        schedule_email_url,
        headers=header,
        json=body,
    )
    return request.json()
