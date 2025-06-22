
from decimal import Decimal
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from domain.product import Product


class SearchInput(BaseModel):
    productId: str = Field(
        description="Product id to search single product",)


@tool("search_product", args_schema=SearchInput, return_direct=True)
def search_product(id: str) -> str:
    """
    Retrive a product by its ID.
    """
    product = Product(
        product_id="123456",
        name="Example Product",
        price=Decimal(19.99),
        quantity=100,
        img_url="http://example.com/image.jpg",
        description="This is an example product.",
        short_description="Example product description.",
        category="Fashion"
    )

    return product.model_dump_json()


ProductTools = [search_product]
