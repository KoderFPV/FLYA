import asyncio
from typing import AsyncGenerator
from agents.chat.chatAgent import ChatAgent
from domain.state import GlobalState
from langgraph.constants import START
from langgraph.graph import StateGraph
from agents.cart.cartAgent import CartAgent
from agents.checkout.checkoutAgent import CheckoutAgent
from agents.info.infoAgent import InfoAgent
from agents.product.productAgent import ProductAgent
from agents.products.productsAgent import ProductsAgent
from agents.router.routerAgent import RouterAgent, Routes


class Agents:
    def __init__(self, model: str, api_key: str):
        self.state_graph = StateGraph(GlobalState)
        self.model = model
        self.api_key = api_key
        self.router = RouterAgent(self.model, self.api_key)

        self._addNodes()
        self._addEdges()

        self.graph = self._build_graph()

    async def stream_graph_updates(
        self,
            user_input: str) -> AsyncGenerator[str, None]:
        loop = asyncio.get_running_loop()

        def get_sync_stream_data():
            for event in self.graph.stream({
                "messages":
                    [{"role": "user", "content": user_input}]}):
                for value in event.values():
                    yield value["messages"][-1].content

        for content in await loop.run_in_executor(None, get_sync_stream_data):
            yield content
            await asyncio.sleep(0.01)

    def _build_graph(self):
        return self.state_graph.compile()

    def _addNodes(self):
        self.state_graph.add_node(Routes.ROUTER.value, self.router.create)
        self.state_graph.add_node(Routes.PRODUCTS.value, ProductsAgent(
            self.model, self.api_key).create)
        self.state_graph.add_node(Routes.PRODUCT.value, ProductAgent(
            self.model, self.api_key).create)
        self.state_graph.add_node(Routes.CART.value, CartAgent(
            self.model, self.api_key).create)
        self.state_graph.add_node(Routes.CHECKOUT.value, CheckoutAgent(
            self.model, self.api_key).create)
        self.state_graph.add_node(Routes.INFO.value, InfoAgent(
            self.model, self.api_key).create)
        self.state_graph.add_node(Routes.CHAT.value, ChatAgent(
            self.model, self.api_key).create)

    def _addEdges(self):
        self.state_graph.add_edge(START, Routes.ROUTER.value)
        self.state_graph.add_conditional_edges(
            Routes.ROUTER.value, self.router.router_conditional_edge)
