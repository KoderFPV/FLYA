from enum import Enum

from agents.baseAgent import BaseAgent
from agents.router.routerPrompts import RouterPrompts
from domain.state import GlobalState
from langchain_core.messages import SystemMessage


class Routes(Enum):
    REGISTRATION = "registration"
    LOGIN = "login"
    PRODUCT = "product"
    PRODUCTS = "products"
    CART = "cart"
    CHECKOUT = "checkout"
    INFO = "info"
    ROUTER = "router"
    CHAT = "chat"


class RouterAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)
        self.prompts = RouterPrompts()

    def create(self, state: GlobalState):
        if self.llm is None:
            raise ValueError("LLM is not initialized.")
        systemMessage = [SystemMessage(content=self.prompts.systemPrompt)]

        response = self.llm.invoke(
            input=systemMessage + list(state["messages"]),
        )

        return {
            "messages": state["messages"],
            "routerState": {"nextNode": response.content},
        }

    def router_conditional_edge(self, state: GlobalState):
        router_state_dict = state["routerState"]
        next_node = router_state_dict["nextNode"]
        shouldRedirect = (
            next_node in [e.value for e in Routes] and next_node != Routes.ROUTER.value
        )

        if shouldRedirect:
            print(f"Redirecting to next node: {next_node}")
            return next_node
        else:
            print(f"Invalid next node: {next_node}. Defaulting to chat.")
            return Routes.CHAT.value

    def get_tools(self):
        return []
