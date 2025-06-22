
from enum import Enum
from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.constants import END
from agents.router.routerPrompts import RouterPrompts
from domain.state import GlobalState


class Routes(Enum):
    PRODUCT = "product"
    PRODUCTS = "products"
    CART = "cart"
    CHECKOUT = "checkout"
    INFO = "info"
    ROUTER = "router"
    CHAT = "chat"


class RouterAgent:
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.api_key = api_key
        self.prompts = RouterPrompts()

        self.setup_llm()

    def create(self, state: GlobalState):
        systemMessage = [SystemMessage(content=self.prompts.systemPrompt)]

        response = self.llm.invoke(
            input=systemMessage + list(state["messages"]),
        )

        return {
            "messages": state["messages"],
            "routerState": {
                "nextNode": response.content
            }
        }

    def setup_llm(self):
        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=1.0,
            max_retries=2,
            google_api_key=self.api_key,
        )

    def router_conditional_edge(self, state: GlobalState):
        router_state_dict = state["routerState"]
        next_node = router_state_dict["nextNode"]
        shouldRedirect = next_node in [
            e.value for e in Routes] and next_node != Routes.ROUTER.value

        if shouldRedirect:
            print(f"Redirecting to next node: {next_node}")
            return next_node
        else:
            print(f"Invalid next node: {next_node}. Defaulting to chat.")
            return Routes.CHAT.value
