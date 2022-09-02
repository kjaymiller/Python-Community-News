from collections import namedtuple
import datetime
import os
import httpx


buttondown_api_key = os.getenv("BUTTONDOWN_API_KEY")
header = {"Authorization": f"Token {buttondown_api_key}"}

schedule_email_url:str = "https://api.buttondown.email/v1/scheduled-emails"
Shownotes = namedtuple("Shownotes", "subject content publish_date")

def build_email_from_content(
    shownotes: Shownotes,
    publish_date: str,
) -> httpx.Response:
    """
    Uses frontmatter to get the subject and returns a partial of the body to be used to schedule the email.
    """
    body = {
        "email_type": "public",
        "body": shownotes.content,
        "subject": subject,
        "publish_date": publish_date,
    }
    request = httpx.post(
        schedule_email_url,
        headers=header,
        json=body,
    )
    return request