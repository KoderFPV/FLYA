from typing import Annotated, Optional, Sequence
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field


class DeliveryAddress(BaseModel):
    delivery_type: Annotated[Optional[int], Field(ge=1, le=100)] = None
    first_name: Annotated[str, Field(min_length=1)]
    last_name: Annotated[str, Field(min_length=1)]
    street: Annotated[str, Field(min_length=1)]
    city: Annotated[str, Field(min_length=1)]
    postal_code: Annotated[str, Field(min_length=1)]
    country: Annotated[str, Field(min_length=1)]
    lockerId: Annotated[str, Field(min_length=0, default='')]


class PaymentMethod(BaseModel):
    payment_type: Annotated[Optional[int], Field(ge=1, le=100)] = None


class CheckoutState(BaseModel):
    messages: Annotated[Sequence[str], add_messages]
    delivery_address: DeliveryAddress
    payment_method: PaymentMethod
    terms_accepted: Annotated[bool, Field(default=False)]
    order_id: Annotated[Optional[str], Field(
        min_length=1, default=None)] = None
