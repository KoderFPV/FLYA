from typing import Annotated

from pydantic import BaseModel, Field


class RegistrationState(BaseModel):
    login: Annotated[str, Field(min_length=6)]
    password: Annotated[str, Field(min_length=6)]
    repeatePassword: Annotated[str, Field(min_length=6)]
    email: Annotated[str, Field(min_length=6)]
    termsOfService: Annotated[bool, Field(default=False)]
