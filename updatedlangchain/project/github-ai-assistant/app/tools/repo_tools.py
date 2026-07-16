"""
Repository Tools

This module exposes GitHub repository related
operations to the LangChain Agent.
"""

from langchain_core.tools import tool

from app.services.github_client import GitHubClient

client = GitHubClient()


@tool
def get_repository(owner: str, repo: str) -> dict:
    """
    Get complete information about a GitHub repository.

    Use this tool whenever the user asks about:

    - repository details
    - stars
    - forks
    - owner
    - description
    - language
    - default branch
    """

    return client.get_repository(owner, repo)


@tool
def repository_summary(owner: str, repo: str) -> str:
    """
    Generate a readable summary of a GitHub repository.
    """

    repository = client.get_repository(owner, repo)

    return f"""
Repository: {repository["full_name"]}

Description:
{repository["description"]}

Primary Language:
{repository["language"]}

Stars:
{repository["stargazers_count"]}

Forks:
{repository["forks_count"]}

Open Issues:
{repository["open_issues_count"]}

Watchers:
{repository["watchers_count"]}

Default Branch:
{repository["default_branch"]}

Repository URL:
{repository["html_url"]}
"""


@tool
def list_languages(owner: str, repo: str) -> dict:
    """
    List all programming languages used
    inside the repository.
    """

    return client.list_languages(owner, repo)


@tool
def list_contributors(owner: str, repo: str) -> list:
    """
    List repository contributors.
    """

    contributors = client.list_contributors(owner, repo)

    return [
        {
            "username": contributor["login"],
            "contributions": contributor["contributions"],
            "profile": contributor["html_url"],
        }
        for contributor in contributors
    ]


@tool
def repository_statistics(owner: str, repo: str) -> dict:
    """
    Return important repository statistics.
    """

    repository = client.get_repository(owner, repo)

    return {
        "Stars": repository["stargazers_count"],
        "Forks": repository["forks_count"],
        "Watchers": repository["watchers_count"],
        "Open Issues": repository["open_issues_count"],
        "Subscribers": repository["subscribers_count"],
    }