from decimal import Decimal
from typing import List
from langchain_core.tools import tool
from domain.cart import CartProduct


@tool("get_checkout_content", return_direct=True)
def get_checkout_content() -> List[str]:
    """
    Retrive informations about current checkout content.
    """

    return [
        CartProduct(
            product_id="123456",
            name="Example Product",
            price=Decimal(19.99),
            quantity=2,
            img_url="http://example.com/image.jpg",
        ).model_dump_json(),
        CartProduct(
            product_id="654321",
            name="Another Product",
            price=Decimal(29.99),
            quantity=1,
            img_url="http://example.com/image2.jpg",
        ).model_dump_json()

    ]


Checkout_tools = [get_checkout_content]
