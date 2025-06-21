from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from agents.cart.cartState import CartState
from agents.checkout.checkoutState import CheckoutState
from agents.info.infoState import InfoState
from agents.product.productState import ProductState
from agents.products.productsState import ProductsState
from agents.router.routerState import RouterState


class GlobalState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int

    infoState: InfoState
    productState: ProductState
    productsState: ProductsState
    cartState: CartState
    checkoutState: CheckoutState
    routerState: RouterState
