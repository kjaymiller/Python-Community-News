import re
from collections import defaultdict, namedtuple
from typing import Any, Generator, Literal

import os
import httpx
from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode

Issue = namedtuple("Issue", "metadata body")
issues:str = "issues"
pulls:str = "pulls"

def get_from_github(issue_id: str|int, request_type: Literal[issues]| Literal[pulls]) -> dict[str, str]:
    """
    Returns the issue with the given id.
    The issue_id must be a valid integer.
    """

    if request_type not in [issues, pulls]:
        raise ValueError("type must be either: issues or pulls")

    url = f"https://api.github.com/repos/kjaymiller/Python-Community-News/{request_type}/{str(issue_id)}"
    headers={
        "Authorization": f"Bearer {os.environ['GITHUB_API_TOKEN']}",
        }
    request = httpx.get(url, headers=headers)
    if request.status_code not in [200, 201]:
        raise ConnectionRefusedError(f"Unable to connect: {request.json()}")
    return request.json()


def get_issues(issues) -> Generator[dict[str, str], None, None]:
    """Returns the issues filed in the last week"""
    for issue in issues:
        issue_content = get_from_github(issue, "issues")
        body = parse_issue_markdown(issue_content['body'])
        i = Issue(metadata=issue_content, body=body)
        yield i


def parse_issue_markdown(text) -> dict:
    """Use markdownit to split at section headings"""
    md = MarkdownIt("zero", {"maxNesting": 1})
    md.enable(["heading", "paragraph"])
    tokens = md.parse(text)
    node = SyntaxTreeNode(tokens)
    issue_object = defaultdict(list)
    for n in node.children:
        if n.type == "heading":
            issue_key = n.children[0].content.lower()
        elif content := n.children[0].content == "_No response_":
            continue
        else:
            issue_object[issue_key].append(n.children[0].content)
        
    for key, value in issue_object.items():
        issue_object[key] = "\n".join(value)

    return issue_object


def get_content_issues(body: dict[str, Any], issues_tag: str) -> Generator[dict[str, str], None, None]:
    """
    Returns Issues Passed in sections of the issue body
    """
    issues = re.findall(r"\d+", body[issues_tag])
    return issues
