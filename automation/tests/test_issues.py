import pytest
from issues import parse_issue_markdown
from engine import engine

def test_issues_markdown_parsing(issue_text):
    """Test the issue text is parsed into segments"""
    issue =  parse_issue_markdown(issue_text)
    assert issue["Issue Name"] == ["Test Issue"]
    assert "Skipped Section" not in issue
    assert len(issue["TextArea Content"]) == 2
