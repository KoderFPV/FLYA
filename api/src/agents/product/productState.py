from typing import Annotated

from domain.product import Product
from pydantic import BaseModel, Field


class ProductState(BaseModel):
    product_id: Annotated[str, Field(min_length=6)]
    product: Product
