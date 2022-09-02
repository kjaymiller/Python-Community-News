"""Script to be ran by GH Actions to build the archive and schedule the newsletter"""

from collections import namedtuple
from src import github
from src import newsletter
from src import engine


def build_shownotes(pr: int) -> None:
    """Build the archive from the issues"""

    pr = github.get_from_github(pr, request_type="issues")
    pr_body = github.parse_issue_markdown(pr["body"])
    issues = list(github.get_issues(github.get_content_issues(pr_body, "issues")))
    cfps = list(github.get_issues(github.get_content_issues(pr_body, "cfps")))
    conferences = list(
        github.get_issues(github.get_content_issues(pr_body, "conferences"))
    )
    template = engine.engine.get_template("newsletter.md")
    content = template.render(
        issues=issues,
        cfps=cfps,
        conferences=conferences,
        podcast=pr_body.get("podcast", [""]),
        youtube=pr_body.get("youtube", [""]),
        publish_date=pr,
    )

    shownotes = newsletter.Shownotes(
        subject=pr["title"],
        content=content,
        publish_date=pr_body["Newsletter Publish"],
    )

    print(content)


if __name__ == "__main__":
    build_shownotes(70)
