from decimal import Decimal
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from domain.product import Product


class SearchInput(BaseModel):
    query: str = Field(
        description="The search query for products, e.g., 'skirt'",)
    page: str = Field(
        description="The page number for pagination, e.g., 1",)


@tool("search_products", args_schema=SearchInput, return_direct=True)
def search_products(query: str, page: int = 1) -> list[str]:
    """
    Search for products based on the query.
    """
    # Simulate a product search
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

    product2 = Product(
        product_id="654321",
        name="Another Product",
        price=Decimal(29.99),
        quantity=50,
        img_url="http://example.com/image2.jpg",
        description="This is another example product.",
        short_description="Another example product description.",
        category="Fashion"
    )

    product3 = Product(
        product_id="789012",
        name="Third Product",
        price=Decimal(39.99),
        quantity=75,
        img_url="http://example.com/image3.jpg",
        description="This is a third example product.",
        short_description="Third example product description.",
        category="Fashion"
    )

    return [
        product.model_dump_json(),
        product2.model_dump_json(),
        product3.model_dump_json()
    ]


Products_tools = [search_products]
