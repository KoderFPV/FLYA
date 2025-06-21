from fastapi import FastAPI
from starlette.responses import StreamingResponse

from agents.agents import Agents


class Server:
    def __init__(self, agents: Agents):
        self.app = FastAPI()
        self.agents = agents

        @self.app.get("/")
        def read_root():
            return {"Hello": "World"}

        @self.app.get("/chat")
        async def chat(user_input: str):
            async def generate_updates():
                async for update in self.agents.stream_graph_updates(user_input):
                    yield update.encode("utf-8") + b"\n"

            return StreamingResponse(generate_updates(), media_type="text/event-stream")

    def get_app(self):
        return self.app
