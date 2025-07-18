from agents.baseAgent import BaseAgent
from agents.info.infoTools import Info_tools


class InfoAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)

    def get_tools(self):
        return Info_tools
