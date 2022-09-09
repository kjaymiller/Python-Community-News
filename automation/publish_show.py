"""Script to be ran by GH Actions to build the archive and schedule the newsletter"""

import pathlib

import typer
from dateutil import parser
from src import newsletter
from src.engine import engine
from src.github import Episode


def build_website(episode: Episode) -> str:
    """Renders the content for the website"""
    template = engine.get_template("archive.md")
    github_filename = parser.isoparse(episode.created_at).strftime("%Y-%m-%d")
    github_path = pathlib.Path(f"./site/content/{github_filename}.md")
    content = template.render(
        title=episode.title,
        date=episode.created_at,
        issues=episode.issues,
        cfps=episode.cfps,
        conferences=episode.conferences,
        podcast=episode.podcast,
        youtube=episode.youtube,
        github=f"https://github.com/kjaymiller/Python-Community-News/blob/main/app/content/{{github_filename}}.md",
    )
    return github_path.write_text(content)


def build_newsletter(episode: Episode) -> dict[str, str]:
    """Build the archive from the issues"""
    template = engine.get_template("newsletter.md")
    content = template.render(
        issues=episode.issues,
        cfps=episode.cfps,
        conferences=episode.conferences,
        podcast=episode.podcast,
        youtube=episode.youtube,
    )

    shownotes = newsletter.Shownotes(
        subject=episode.title,
        content=content,
        publish_date=episode.newsletter_publish,
    )

    # print(shownotes)
    return newsletter.build_email_from_content(shownotes)


def main(episode: int):
    """Build the archive and schedule the newsletter"""
    episode = Episode(episode, ["issues", "cfps", "conferences"])
    build_website(episode)
    build_newsletter(episode)


if __name__ == "__main__":
    typer.run(main)
