"""Script to be ran by GH Actions to build the archive"""

from collections import namedtuple
from typer import Typer
from src import github
from src import newsletter
from src import engine





def parse_issues(pr: int) -> None:
    """Build the archive from the issues"""

    pr = github.get_from_github(issue, request_type)
    pr_body = github.parse_issue_markdown(issue_response['body'])
    issues = list(github.get_issues(github.get_content_issues(issue_body, "issues")))
    cfps = list(github.get_issues(github.get_content_issues(issue_body, "cfps")))
    conferences = list(github.get_issues(github.get_content_issues(issue_body, "conferences")))
    template = engine.engine.get_template("newsletter.md")
    content = template.render(
        issues=issues,
        cfps=cfps,
        conferences=conferences,
        podcast=issue_body.get('podcast', ['']),
        youtube=issue_body.get('youtube', ['']),
        publish_date=pr
    )

    shownotes = Shownotes(
        subject=issue_response['title'],
        content=content,
        publish_date=i,)




if __name__ == "__main__":
    build_shownotes(70)