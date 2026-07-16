"""
GitHub Search Tools

Expose GitHub Search API to LangChain.
"""

from langchain_core.tools import tool

from app.services.github_client import GitHubClient

client = GitHubClient()


@tool
def search_code(query: str):
    """
    Search GitHub code.

    Examples:
    - JWT authentication repo:microsoft/vscode
    - Dockerfile repo:langchain-ai/langchain
    - TODO repo:facebook/react
    """

    response = client.search_code(query)

    items = response.get("items", [])

    results = []

    for item in items[:10]:

        results.append(
            {
                "file_name": item["name"],
                "repository": item["repository"]["full_name"],
                "path": item["path"],
                "url": item["html_url"],
            }
        )

    return results


@tool
def search_todos(owner: str, repo: str):
    """
    Search all TODO comments inside a repository.
    """

    return search_code.invoke(
        {
            "query": f"TODO repo:{owner}/{repo}"
        }
    )


@tool
def search_authentication(owner: str, repo: str):
    """
    Search authentication related code.
    """

    return search_code.invoke(
        {
            "query": f"authentication OR login repo:{owner}/{repo}"
        }
    )


@tool
def search_api_routes(owner: str, repo: str):
    """
    Search API routes.
    """

    return search_code.invoke(
        {
            "query": f"router OR app.get OR app.post repo:{owner}/{repo}"
        }
    )


@tool
def search_react_components(owner: str, repo: str):
    """
    Search React Components.
    """

    return search_code.invoke(
        {
            "query": f"function OR const repo:{owner}/{repo} extension:tsx"
        }
    )


@tool
def search_python_classes(owner: str, repo: str):
    """
    Search Python classes.
    """

    return search_code.invoke(
        {
            "query": f"class repo:{owner}/{repo} language:Python"
        }
    )


@tool
def search_docker(owner: str, repo: str):
    """
    Search Docker related files.
    """

    return search_code.invoke(
        {
            "query": f"Dockerfile repo:{owner}/{repo}"
        }
    )


@tool
def search_github_actions(owner: str, repo: str):
    """
    Search GitHub Actions workflows.
    """

    return search_code.invoke(
        {
            "query": f".github/workflows repo:{owner}/{repo}"
        }
    )


@tool
def search_repositories(query: str):
    """
    Search GitHub repositories.
    """

    response = client.search_repositories(query)

    repositories = response.get("items", [])

    return [
        {
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"],
            "description": repo["description"],
            "url": repo["html_url"],
        }
        for repo in repositories[:10]
    ]    