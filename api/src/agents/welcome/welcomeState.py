from typing import Annotated, Sequence
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field


class WelcomeState(BaseModel):
    messages: Annotated[Sequence[str], add_messages]
    welcome_message: Annotated[str, Field(
        min_length=1)] = "Welcome to our store! How can I assist you today?"
