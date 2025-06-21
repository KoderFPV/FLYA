from decimal import Decimal
from typing import Annotated
from pydantic import BaseModel, Field


class Product(BaseModel):
    product_id: Annotated[str, Field(min_length=6)]
    name: Annotated[str, Field(min_length=3)]
    price: Annotated[Decimal, Field(gt=Decimal('0.00'))]
    quantity: Annotated[int, Field(gt=0)]
    img_url: Annotated[str, Field(min_length=1)]
    description: Annotated[str, Field(min_length=1)] = ""
    short_description: Annotated[str, Field(min_length=1)] = ""
    category: Annotated[str, Field(min_length=1)] = ""
