from agents.baseAgent import BaseAgent
from agents.checkout.checkoutTools import Checkout_tools


class CheckoutAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)

    def get_tools(self):
        return Checkout_tools
