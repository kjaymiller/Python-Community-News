import httpx
import os
import datetime
import pathlib
import frontmatter
import engine
from issues import get_issue, parse_issue_markdown

hour = str
minute = str
buttondown_api_key = os.getenv('BUTTONDOWN_API_KEY')
header = {'Authorization': f'Token {buttondown_api_key}'}

schedule_email_url = "https://api.buttondown.email/v1/scheduled-emails"


def get_show_file(
    directory: pathlib.Path,
    date:datetime.datetime
) -> pathlib.Path:
    """Get the file for the last show"""
    show_date = date.strftime("%Y-%m-%d")
    show_file = pathlib.Path(directory).joinpath(show_date).with_suffix(".md") 
    return show_file


def get_publish_time(
    date:datetime.datetime,
    time:datetime.time,
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
    subject = content.metadata.get('subject')
    body={
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


def load_newsletter_issues(episode_issue: dict[str, str]) -> list[dict[str, str]]:
    """
    Loads the issues from the file and returns the template show the newsletter.
    """
    
    issue = get_issue(episode_issue)
    md = parse_issue_markdown(issue)
    print(md)


if __name__ == "__main__":
    load_newsletter_issues(34)