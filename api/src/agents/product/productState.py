from typing import Annotated, Sequence
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from domain.product import Product


class ProductState(BaseModel):
    messages: Annotated[Sequence[str], add_messages]
    product_id: Annotated[str, Field(min_length=6)]
    product: Product
