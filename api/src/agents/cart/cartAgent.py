from agents.baseAgent import BaseAgent
from agents.cart.cartTools import Cart_tools


class CartAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)

    def get_tools(self):
        return Cart_tools
