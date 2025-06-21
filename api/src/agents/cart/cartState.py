
from decimal import Decimal
from typing import Annotated, Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    product_id: Annotated[str, Field(min_length=6)]
    name: Annotated[str, Field(min_length=3)]
    price: Annotated[Decimal, Field(gt=Decimal('0.00'))]
    quantity: Annotated[int, Field(gt=0)]
    img_url: Annotated[str, Field(min_length=1)]

class ChatState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    cartItems: list[ProductSchema] 
    cartTotal: Annotated[Decimal, Field(gt=Decimal('0.00'))]
