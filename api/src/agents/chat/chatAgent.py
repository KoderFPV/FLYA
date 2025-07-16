from domain.state import GlobalState
from langchain_google_genai import ChatGoogleGenerativeAI


class ChatAgent:
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.api_key = api_key

        self.setup_llm()

    def create(self, state: GlobalState):
        return {"messages": [self.llm.invoke(state["messages"])]}

    def setup_llm(self):
        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=0,
            max_retries=2,
            google_api_key=self.api_key,
        )
