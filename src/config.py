"""
This module contains configuration variables for the application.
"""

from utils.environment import get_env_var

GITHUB_PRIVATE_KEY = get_env_var("PRIVATE_KEY")
GITHUB_APP_ID = int(get_env_var("APP_ID"))
if GITHUB_PRIVATE_KEY.endswith(".pem"):
    with open(GITHUB_PRIVATE_KEY, "r", encoding="utf-8") as key_file:
        GITHUB_PRIVATE_KEY = key_file.read()
GITHUB_INSTALLATION_ID = get_env_var("INSTALLATION_ID", default=None)

GITHUB_REPOSITORY = get_env_var("GITHUB_REPOSITORY").split("/")
GITHUB_REPOSITORY_OWNER = GITHUB_REPOSITORY[0]
GITHUB_REPOSITORY_NAME = GITHUB_REPOSITORY[1]

OPENAI_API_KEY = get_env_var("OPENAI_API_KEY")
OPENAI_MODEL = get_env_var("OPENAI_MODEL")

CREDENTIALS_CONTENT = get_env_var("GOOGLE_CREDENTIALS_CONTENT", default='')
SPREADSHEET_URL = get_env_var("SPREADSHEET", default='')

DEFAULT_PROMPT = """You are a teacher reviewing a student's code.
You should give only advices, not complete code.
Check code for different conventions, and give advices about best practices.
Send response in format for leaving comment to pull request.
Use markup as it will be posted on GitHub.
It will be posted on github, so use markups inside body
The student has submitted the following files for review:"""

PROMPT = get_env_var("PROMPT", default=DEFAULT_PROMPT)

LOGGING_LEVEL = get_env_var("LOGGING_LEVEL", default="INFO")
