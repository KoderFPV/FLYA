from langchain_core.tools import tool
from pydantic import BaseModel, Field


class LoginForm(BaseModel):
    email: str = Field(
        description="The search query for products, e.g., 'skirt'",
    )
    password: str = Field(
        description="The page number for pagination, e.g., 1",
    )


@tool("login_user", args_schema=LoginForm, return_direct=True)
def login(email: str, password: str) -> str:
    """
    Login a user with the provided email and password.
    """

    if not email or not password:
        return "Email and password are required for login."

    if email == "artur.slomowski@gmail.com" and password == "Koder!23!23":
        return f"User logged in successfully with email: {email}"

    return "Invalid email or password. Please try again."


Login_tools = [login]
