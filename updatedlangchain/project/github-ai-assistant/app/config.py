"""
Application configuration.

This module loads all environment variables
and exposes them through a single settings object.
"""

from dotenv import load_dotenv
import os

# Load variables from .env into the environment
load_dotenv()


class Settings:
    """
    Stores application configuration.

    Every setting is read only once during startup.
    """

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    GITHUB_BASE_URL = "https://api.github.com"

    MODEL_NAME = "llama-3.3-70b-versatile"


settings = Settings()