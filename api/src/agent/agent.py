import asyncio
from langgraph.graph import StateGraph, START
from langchain_google_genai import ChatGoogleGenerativeAI
from states.chatState import ChatState
from typing import AsyncGenerator


class Agent:
    def __init__(self, model: str, api_key: str):
        self.api_key = api_key
        self.graph_builder = StateGraph(ChatState)
        self.llm = ChatGoogleGenerativeAI(
            model=model,
            temperature=1.0,
            max_retries=2,
            google_api_key=self.api_key,
        )
        self.graph = self._build_graph()

    async def stream_graph_updates(self, user_input: str) -> AsyncGenerator[str, None]:
        loop = asyncio.get_running_loop()

        def get_sync_stream_data():
            for event in self.graph.stream({"messages": [{"role": "user", "content": user_input}]}):
                for value in event.values():
                    yield value["messages"][-1].content

        for content in await loop.run_in_executor(None, get_sync_stream_data):
            yield content
            await asyncio.sleep(0.01)

    def _chatbot(self, state: ChatState):
        return {"messages": [self.llm.invoke(state["messages"])]}

    def _build_graph(self):
        self.graph_builder.add_node("chatbot", self._chatbot)
        self.graph_builder.add_edge(START, "chatbot")
        return self.graph_builder.compile()
