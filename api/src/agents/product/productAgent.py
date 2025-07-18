from agents.baseAgent import BaseAgent
from agents.product.productTools import Product_tools


class ProductAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)

    def get_tools(self):
        return Product_tools
