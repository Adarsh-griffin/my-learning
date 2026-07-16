"""
GitHub API Client

This module provides a reusable wrapper around the GitHub REST API.
All communication with GitHub should happen through this client.
"""

from typing import Any

import httpx

from app.config import settings


class GitHubClient:
    """Reusable GitHub REST API Client."""

    def __init__(self):
        self.client = httpx.Client(
            base_url=settings.GITHUB_BASE_URL,
            headers={
                "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=30.0,
        )

    # --------------------------------------------------
    # Internal Helper Methods
    # --------------------------------------------------

    def _get(self, endpoint: str, params: dict | None = None) -> Any:
        """Perform a GET request."""

        response = self.client.get(
            endpoint,
            params=params,
        )

        response.raise_for_status()

        return response.json()

    def _post(self, endpoint: str, json: dict | None = None) -> Any:
        """Perform a POST request."""

        response = self.client.post(
            endpoint,
            json=json,
        )

        response.raise_for_status()

        return response.json()

    def _patch(self, endpoint: str, json: dict | None = None) -> Any:
        """Perform a PATCH request."""

        response = self.client.patch(
            endpoint,
            json=json,
        )

        response.raise_for_status()

        return response.json()

    # --------------------------------------------------
    # Repository Methods
    # --------------------------------------------------

    def get_repository(
        self,
        owner: str,
        repo: str,
    ):
        """
        Fetch repository details.
        """

        return self._get(
            f"/repos/{owner}/{repo}"
        )

    def list_languages(
        self,
        owner: str,
        repo: str,
    ):
        """
        Get languages used in repository.
        """

        return self._get(
            f"/repos/{owner}/{repo}/languages"
        )

    def list_contributors(
        self,
        owner: str,
        repo: str,
    ):
        """
        List repository contributors.
        """

        return self._get(
            f"/repos/{owner}/{repo}/contributors"
        )

    # --------------------------------------------------
    # Issues
    # --------------------------------------------------

    def list_issues(
        self,
        owner: str,
        repo: str,
        state: str = "open",
    ):
        """
        List repository issues.
        """

        return self._get(
            f"/repos/{owner}/{repo}/issues",
            params={
                "state": state,
            },
        )

    def create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: str = "",
    ):
        """
        Create a GitHub Issue.
        """

        return self._post(
            f"/repos/{owner}/{repo}/issues",
            json={
                "title": title,
                "body": body,
            },
        )

    # --------------------------------------------------
    # Pull Requests
    # --------------------------------------------------

    def list_pull_requests(
        self,
        owner: str,
        repo: str,
        state: str = "open",
    ):
        """
        List pull requests.
        """

        return self._get(
            f"/repos/{owner}/{repo}/pulls",
            params={
                "state": state,
            },
        )

    # --------------------------------------------------
    # Commits
    # --------------------------------------------------

    def list_commits(
        self,
        owner: str,
        repo: str,
    ):
        """
        List repository commits.
        """

        return self._get(
            f"/repos/{owner}/{repo}/commits"
        )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search_code(
        self,
        query: str,
    ):
        """
        Search code across GitHub.
        """

        return self._get(
            "/search/code",
            params={
                "q": query,
            },
        )

    # --------------------------------------------------
    # Close Client
    # --------------------------------------------------

    def close(self):
        """
        Close underlying HTTP client.
        """

        self.client.close()


    def search_repositories(
        self,
        query: str,
    ):
        """
        Search GitHub repositories.
        """

        return self._get(
            "/search/repositories",
            params={
                "q": query,
            },
        )   