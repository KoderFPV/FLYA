from enum import Enum
from typing import Annotated, Sequence
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field


class InfoPage(Enum):
    TERMS = "terms"
    ORDER = "order_confirmation"
    DELIVERY = "delivery_address"
    PAYMENT = "payment_method"
    CONTACT = "contact_info"


class InfoState(BaseModel):
    messages: Annotated[Sequence[str], add_messages]
    page_type: Annotated[InfoPage, Field(default=None)]
    page_content: Annotated[str, Field(default="")]
