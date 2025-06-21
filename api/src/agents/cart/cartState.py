
from decimal import Decimal
from typing import Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from domain.cart import CartProduct


class CartState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    cartItems: list[CartProduct]
    cartTotal: Annotated[Decimal, Field(gt=Decimal('0.00'))]
