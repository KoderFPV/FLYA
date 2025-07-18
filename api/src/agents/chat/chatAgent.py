from agents.baseAgent import BaseAgent


class ChatAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)
