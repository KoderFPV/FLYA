
from typing import Protocol, AsyncGenerator
from fastapi import FastAPI
from starlette.responses import StreamingResponse


class AgentProtocol(Protocol):
    async def stream_graph_updates(self, user_input: str) -> AsyncGenerator[str, None]:
        pass


class Server:
    def __init__(self, agent: AgentProtocol):
        self.app = FastAPI()
        self.agent = agent

        @self.app.get("/")
        def read_root():
            return {"Hello": "World"}

        @self.app.get("/chat")
        async def chat(user_input: str):
            """
            Endpoint do strumieniowania aktualizacji z agenta.
            """
            async def generate_updates():
                async for update in self.agent.stream_graph_updates(user_input):
                    yield update.encode("utf-8") + b"\n"

            return StreamingResponse(generate_updates(), media_type="text/event-stream")
