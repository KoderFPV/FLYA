
from typing import Annotated
from pydantic import BaseModel, Field


class Routes(BaseModel):
    routes: int


class RouterState(BaseModel):
    nextNode: Annotated[str, Field(min_length=1)]
