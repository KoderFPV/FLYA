from abc import ABC, abstractmethod

from domain.state import GlobalState
from langchain_google_genai import ChatGoogleGenerativeAI


class BaseAgent(ABC):
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.api_key = api_key
        self.llm = None
        self.setup_llm()

    def create(self, state: GlobalState):
        if self.llm is None:
            raise ValueError("LLM has not been set up. Call setup_llm() first.")

        return {"messages": [self.llm.invoke(state["messages"])]}

    def setup_llm(self):
        tools = self.get_tools()
        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=0,
            max_retries=2,
            google_api_key=self.api_key,
        ).bind_tools(tools)

    def get_tools(self):
        return []
