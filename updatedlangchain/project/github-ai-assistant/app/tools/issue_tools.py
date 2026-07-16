"""
GitHub Issue Tools

LangChain tools for interacting with GitHub Issues.
"""

from langchain_core.tools import tool

from app.services.github_client import GitHubClient

client = GitHubClient()


@tool
def list_open_issues(owner: str, repo: str) -> list:
    """
    List all open issues in a GitHub repository.

    Use this when the user asks:
    - Show open issues
    - List bugs
    - What issues are open?
    """

    issues = client.list_issues(
        owner=owner,
        repo=repo,
        state="open",
    )

    return [
        {
            "number": issue["number"],
            "title": issue["title"],
            "author": issue["user"]["login"],
            "url": issue["html_url"],
        }
        for issue in issues
    ]


@tool
def list_closed_issues(owner: str, repo: str) -> list:
    """
    List all closed issues.
    """

    issues = client.list_issues(
        owner=owner,
        repo=repo,
        state="closed",
    )

    return [
        {
            "number": issue["number"],
            "title": issue["title"],
            "author": issue["user"]["login"],
            "url": issue["html_url"],
        }
        for issue in issues
    ]


@tool
def latest_issue(owner: str, repo: str) -> dict:
    """
    Return the latest issue in the repository.
    """

    issues = client.list_issues(
        owner=owner,
        repo=repo,
        state="open",
    )

    if not issues:
        return {
            "message": "No open issues found."
        }

    issue = issues[0]

    return {
        "number": issue["number"],
        "title": issue["title"],
        "author": issue["user"]["login"],
        "created_at": issue["created_at"],
        "url": issue["html_url"],
    }


@tool
def issue_count(owner: str, repo: str) -> str:
    """
    Return the total number of open issues.
    """

    issues = client.list_issues(
        owner=owner,
        repo=repo,
        state="open",
    )

    return f"{len(issues)} open issues found."


@tool
def summarize_issues(owner: str, repo: str) -> str:
    """
    Summarize the first five open issues.
    """

    issues = client.list_issues(
        owner=owner,
        repo=repo,
        state="open",
    )

    if not issues:
        return "No open issues."

    summary = []

    for issue in issues[:5]:

        summary.append(
            f"""
Issue #{issue["number"]}

Title:
{issue["title"]}

Author:
{issue["user"]["login"]}

Created:
{issue["created_at"]}

URL:
{issue["html_url"]}
"""
        )

    return "\n".join(summary)


@tool
def create_issue(
    owner: str,
    repo: str,
    title: str,
    body: str,
):
    """
    Create a GitHub issue.

    Use this tool whenever the user asks
    to create or open an issue.
    """

    return client.create_issue(
        owner=owner,
        repo=repo,
        title=title,
        body=body,
    )