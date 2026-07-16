"""
GitHub AI Agent

This is the brain of the application.
The agent decides which GitHub tool to call
based on the user's request.
"""

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from app.config import settings

# Repository Tools
from app.tools.repo_tools import (
    get_repository,
    repository_summary,
    list_languages,
    list_contributors,
    repository_statistics,
)

# Issue Tools
from app.tools.issue_tools import (
    list_open_issues,
    list_closed_issues,
    latest_issue,
    issue_count,
    summarize_issues,
    create_issue,
)

# Search Tools
from app.tools.search_tools import (
    search_code,
    search_repositories,
    search_authentication,
    search_api_routes,
    search_react_components,
    search_python_classes,
    search_docker,
    search_github_actions,
)

# ---------------------------------------------------------
# LLM
# ---------------------------------------------------------

llm = init_chat_model(
    settings.MODEL_NAME,
    model_provider="groq",
)

# ---------------------------------------------------------
# System Prompt
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are an expert GitHub Developer Assistant.

You help developers understand repositories,
issues, pull requests and source code.

Rules:

- Always use tools whenever live GitHub data is required.
- Never hallucinate repository information.
- If a repository does not exist,
  explain the error politely.
- Give concise but useful answers.
- Summarize large outputs.
"""

# ---------------------------------------------------------
# Register Every Tool
# ---------------------------------------------------------

TOOLS = [

    # Repository
    get_repository,
    repository_summary,
    repository_statistics,
    list_languages,
    list_contributors,

    # Issues
    list_open_issues,
    list_closed_issues,
    latest_issue,
    issue_count,
    summarize_issues,
    create_issue,

    # Search
    search_code,
    search_repositories,
    search_authentication,
    search_api_routes,
    search_react_components,
    search_python_classes,
    search_docker,
    search_github_actions,
]

# ---------------------------------------------------------
# Create Agent
# ---------------------------------------------------------

agent = create_agent(
    model=llm,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT,
)