import pytest
import datetime
import random

@pytest.fixture(scope="session")
def date():
    return datetime.datetime.today()

@pytest.fixture(scope="session")
def time():
    return datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))

@pytest.fixture(scope="session")
def shownotes_text():
    return """---
subject: Test Newsletter
---

This is some text for the newsletter.
"""

@pytest.fixture(scope="session")
def newsletter_body():
    return {
        "email_type": "public",
        "body": "This is some text for the newsletter.",
        "subject": "Test Newsletter",
    }