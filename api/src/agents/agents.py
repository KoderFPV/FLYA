import asyncio
from enum import Enum
from typing import Any, AsyncGenerator, List, Union
from agents.chat.chatAgent import ChatAgent
from agents.products.productsTools import ProductsTools
from domain.state import GlobalState
from langgraph.constants import END, START
from langgraph.graph import StateGraph
from agents.cart.cartAgent import CartAgent
from agents.checkout.checkoutAgent import CheckoutAgent
from agents.info.infoAgent import InfoAgent
from agents.product.productAgent import ProductAgent
from agents.products.productsAgent import ProductsAgent
from agents.router.routerAgent import RouterAgent, Routes
from langgraph.prebuilt import ToolNode, tools_condition


class Tools(Enum):
    PRODUCTS = "ProductsTools"


class Agents:
    def __init__(self, model: str, api_key: str):
        self.state_graph = StateGraph(GlobalState)
        self.model = model
        self.api_key = api_key
        self.router = RouterAgent(self.model, self.api_key)

        self._addNodes()
        self._addToolNodes()

        self._addRoutingEdges()
        self._addProductsEdges()

        self.graph = self._build_graph()
        self.graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

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

    def _addToolNodes(self):
        productsToolNode = ToolNode(tools=ProductsTools)

        self.state_graph.add_node(Tools.PRODUCTS.value, productsToolNode)

    def _addRoutingEdges(self):
        self.state_graph.add_edge(START, Routes.ROUTER.value)
        self.state_graph.add_conditional_edges(
            Routes.ROUTER.value, self.router.router_conditional_edge, {
                Routes.PRODUCT.value: Routes.PRODUCT.value,
                Routes.PRODUCTS.value: Routes.PRODUCTS.value,
                Routes.CART.value: Routes.CART.value,
                Routes.CHECKOUT.value: Routes.CHECKOUT.value,
                Routes.INFO.value: Routes.INFO.value,
                Routes.CHAT.value: Routes.CHAT.value,
                END: END
            })

    def _addProductsEdges(self):
        self.state_graph.add_conditional_edges(
            Routes.PRODUCTS.value,
            self.custom_route_tools(Tools.PRODUCTS.value),
            {
                Tools.PRODUCTS.value: Tools.PRODUCTS.value,
                END: END,
            }
        )
        self.state_graph.add_edge(Tools.PRODUCTS.value, Routes.PRODUCTS.value)

    def custom_route_tools(self, nodeName: str):
        def route_tools(state: GlobalState):
            """
            Use in the conditional_edge to route to the ToolNode if the last message
            has tool calls. Otherwise, route to the end.
            """
            if isinstance(state, list):
                ai_message = state[-1]
            elif messages := state.get("messages", []):
                ai_message = messages[-1]
            else:
                raise ValueError(
                    f"No messages found in input state to tool_edge: {state}")
            if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
                return nodeName
            return END

        return route_tools
