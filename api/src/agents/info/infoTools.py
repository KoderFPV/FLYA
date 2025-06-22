
from enum import Enum
from typing import List
from langchain_core.tools import tool
from pydantic import BaseModel, Field


class Information(Enum):
    Delivery = "Delivery"
    Payment = "Payment"
    About_company = "About_company"


class SearchInput(BaseModel):
    productId: str = Field(
        description="Product id to search single product",)


@tool("search_informations", args_schema=SearchInput, return_direct=True)
def search_informations(type: Information) -> List[str]:
    """
    Retrive informations about ecommerce shop like delivery, payment, and company information.
    """
    if type == Information.Delivery:
        return ["Delivery information: We deliver worldwide within 5-7 business days."]
    elif type == Information.Payment:
        return ["Payment information: We accept all major credit cards and PayPal."]
    elif type == Information.About_company:
        return ["About company: We are a leading ecommerce platform with a wide range of products."]
    else:
        return ["Invalid information type. Please choose Delivery, Payment, or About_company."]


Info_tools = [search_informations]
