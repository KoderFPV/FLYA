from typing import Annotated
from pydantic import BaseModel, Field
from domain.product import Product


class ProductState(BaseModel):
    product_id: Annotated[str, Field(min_length=6)]
    product: Product
