import asyncio
from enum import Enum
from typing import AsyncGenerator
from agents.cart.cartTools import Cart_tools
from agents.chat.chatAgent import ChatAgent
from agents.checkout.checkoutTools import Checkout_tools
from agents.info.infoTools import Info_tools
from agents.product.productTools import Product_tools
from agents.products.productsTools import Products_tools
from domain.state import GlobalState
from langgraph.constants import END, START
from langgraph.graph import StateGraph
from agents.cart.cartAgent import CartAgent
from agents.checkout.checkoutAgent import CheckoutAgent
from agents.info.infoAgent import InfoAgent
from agents.product.productAgent import ProductAgent
from agents.products.productsAgent import ProductsAgent
from agents.router.routerAgent import RouterAgent, Routes
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver


class Tools(Enum):
    PRODUCTS = "products_tools"
    PRODUCT = "product_tools"
    INFO = "info_tools"
    CHECKOUT = "checkout_tools"
    CART = "cart_tools"


class Agents:
    def __init__(self, model: str, api_key: str):
        self.state_graph = StateGraph(GlobalState)
        self.model = model
        self.api_key = api_key
        self.router = RouterAgent(self.model, self.api_key)

        self._addNodes()
        self._addToolNodes()

        self._addRoutingEdges()

        self._addToolsEdges()

        self.graph = self._build_graph()
        self.graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

    async def stream_graph_updates(
        self,
            user_input: str,
            threadId: str) -> AsyncGenerator[str, None]:
        loop = asyncio.get_running_loop()

        def get_sync_stream_data():
            config = {"configurable": {"thread_id": threadId}}
            for event in self.graph.stream({
                "messages": [{"role": "user", "content": user_input}]
            }, config):
                for value in event.values():
                    yield value["messages"][-1].content

        for content in await loop.run_in_executor(None, get_sync_stream_data):
            yield content
            await asyncio.sleep(0.01)

    def _build_graph(self):
        memory = MemorySaver()
        return self.state_graph.compile(checkpointer=memory)

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
        products_tools_node = ToolNode(tools=Products_tools)
        product_tool_node = ToolNode(tools=Product_tools)
        info_tool_node = ToolNode(tools=Info_tools)
        checkout_tool_node = ToolNode(tools=Checkout_tools)
        cart_tool_node = ToolNode(tools=Cart_tools)

        self.state_graph.add_node(Tools.PRODUCTS.value, products_tools_node)
        self.state_graph.add_node(Tools.PRODUCT.value, product_tool_node)
        self.state_graph.add_node(Tools.INFO.value, info_tool_node)
        self.state_graph.add_node(Tools.CHECKOUT.value, checkout_tool_node)
        self.state_graph.add_node(Tools.CART.value, cart_tool_node)

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
            })

    """ Helpers """

    def _addToolsEdges(self):
        self._addToolsEdge(Routes.PRODUCTS, Tools.PRODUCTS)
        self._addToolsEdge(Routes.PRODUCT, Tools.PRODUCT)
        self._addToolsEdge(Routes.INFO, Tools.INFO)
        self._addToolsEdge(Routes.CHECKOUT, Tools.CHECKOUT)
        self._addToolsEdge(Routes.CART, Tools.CART)

    def _addToolsEdge(self, route: Routes, tool: Tools):
        self.state_graph.add_conditional_edges(
            route.value,
            self.custom_route_tools(tool.value),
            {
                tool.value: tool.value,
                END: END,
            }
        )
        self.state_graph.add_edge(tool.value, route.value)

    def custom_route_tools(self, nodeName: str):
        def route_tools(state: GlobalState):
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
