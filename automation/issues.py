def get_issues_from_github(labels, since_date):
    """Returns the issues filed in the last week"""
    url = "https://api.github.com/repos/kjaymiller/Python-Community-News/issues"
    params = {"labels": ",".join(labels), "since": since_date}
    request = httpx.get(url, params=params)
    return request.json()
