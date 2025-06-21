from typing import Annotated, Sequence
from pydantic import BaseModel, Field


class ProductItem(BaseModel):
    product_id: Annotated[str, Field(min_length=6)]
    name: Annotated[str, Field(min_length=3)]
    price: Annotated[float, Field(gt=0.0)]
    short_description: Annotated[str, Field(min_length=1)]
    img_url: Annotated[str, Field(min_length=1)]


class ProductsState(BaseModel):
    products_list: Annotated[Sequence[ProductItem], Field()]
