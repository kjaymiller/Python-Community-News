from collections import defaultdict
from markdown_it.presets import zero
from markdown_it.tree import SyntaxTreeNode
from markdown_it import MarkdownIt
import datetime
import httpx
from typing import Generator
import re


def get_issue(issue_id: str) -> dict[str, str]:
    """Returns the issue with the given id"""
    url = f"https://api.github.com/repos/kjaymiller/Python-Community-News/issues/{issue_id}" # TODO: remove hardcoded issue url
    request = httpx.get(url)
    return request.json()

def get_issues(labels, since_date: datetime.datetime | None) -> list:
    """Returns the issues filed in the last week"""
    url = "https://api.github.com/repos/kjaymiller/Python-Community-News/issues"
    params = {"labels": ",".join(labels), "since": since_date}
    request = httpx.get(url, params=params)
    return request.json()


def parse_issue_markdown(text) -> dict:
    """Use markdownit to split at section headings"""
    md = MarkdownIt("zero", {"maxNesting": 1})
    md.enable(["heading", "paragraph"])
    tokens = md.parse(text)
    node = SyntaxTreeNode(tokens)
    issue_object = defaultdict(list)
    for n in node.children:
        if n.type == "heading":
            issue_key = (n.children[0].content)
        elif content:= n.children[0].content == "_No response_":
            continue
        else:
            issue_object[issue_key].append(n.children[0].content)
    return issue_object


def get_content_issues(body, issues_tag: str) -> Generator[dict[str, str], None, None]:
    """
    Loads the issues from the file and returns the template show the newsletter.
    """
    md = parse_issue_markdown(body)

    if issues_tag not in md:
        raise ValueError(f"{issues_tag} is required in the issue")

    issues = re.findall(r'\d+', md[issues_tag][0])
    return issues
    