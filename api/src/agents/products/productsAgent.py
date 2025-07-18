from agents.baseAgent import BaseAgent
from agents.products.productsTools import Products_tools


class ProductsAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)

    def get_tools(self):
        return Products_tools
