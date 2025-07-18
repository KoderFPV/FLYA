from agents.baseAgent import BaseAgent
from agents.login.loginTools import Login_tools
from agents.registration.registrationPrompt import RegistrationPrompts


class LoginAgent(BaseAgent):
    def __init__(self, model: str, api_key: str):
        super().__init__(model, api_key)

    def get_tools(self):
        return Login_tools
