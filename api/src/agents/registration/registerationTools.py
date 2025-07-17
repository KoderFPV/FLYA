from agents.registration.registrationService import (is_email,
                                                     is_strong_password)
from langchain_core.tools import tool
from pydantic import BaseModel, Field


class RegistrationForm(BaseModel):
    email: str = Field(
        description="The search query for products, e.g., 'skirt'",
    )
    password: str = Field(
        description="The page number for pagination, e.g., 1",
    )


@tool("register_new_user", args_schema=RegistrationForm, return_direct=True)
def registration(email: str, password: str) -> str:
    """
    Register a new user with the provided email and password.
    """

    if not email or not password:
        return "Email and password are required for registration."

    if is_email(email) is False:
        return "Invalid email format. Please provide a valid email address."

    if is_strong_password(password) is False:
        return (
            "Weak password. Please provide a stronger password that meets the criteria."
        )

    # In a real application, you would save the user to a database here
    return f"User registered successfully with email: {email}"


Registration_tools = [registration]
