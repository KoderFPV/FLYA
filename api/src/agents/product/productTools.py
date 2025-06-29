from decimal import Decimal
from typing import List
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from domain.product import Product


class SearchInput(BaseModel):
    productId: str = Field(
        description="Product id to search single product",)


@tool("search_product", args_schema=SearchInput, return_direct=True)
def search_product(id: str) -> List[str]:
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

    return [product.model_dump_json()]


@tool("add_product_to_cart", return_direct=True)
def add_product_to_cart(product_id: str, quantity: int) -> str:
    """
    Add a product to the shopping cart.
    """
    # This is a placeholder for the actual implementation
    return f"Product {product_id} with quantity {quantity} added to cart."


Product_tools = [search_product]
