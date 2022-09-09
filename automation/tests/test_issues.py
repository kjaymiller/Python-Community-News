import pytest

from automation.issues import get_content_issues, parse_issue_markdown


def test_issues_markdown_parsing(issue_text):
    """Test the issue text is parsed into segments"""
    issue = parse_issue_markdown(issue_text)
    assert issue["Issue Name"] == ["Test Issue"]
    assert "Skipped Section" not in issue
    assert len(issue["TextArea Content"]) == 2


def test_malformed_newsletter_issue_raises_issue():
    bad_issue = """### Issue Name
There's no issues in here
"""
    with pytest.raises(ValueError):
        get_content_issues(bad_issue, "Issue")


def test_valid_issue_returns_issue_list(issue_text):
    assert list(get_content_issues(issue_text, "Issues")) == ["1", "2", "3", "4"]
