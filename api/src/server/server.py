import json

from agents.agents import Agents
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import StreamingResponse


class ChatBody(BaseModel):
    message: str
    threadId: str


class Server:
    def __init__(self, agents: Agents):
        self.app = FastAPI()
        self.agents = agents
        self.router = APIRouter()

        origins = [
            "http://localhost",
            "http://localhost:3000",
        ]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @self.app.get("/")
        def read_root():
            return {"Hello": "World"}

        @self.app.post("/chat")
        async def chat(body: ChatBody):
            async def generate_updates():
                async for update in self.agents.stream_graph_updates(
                    body.message, body.threadId
                ):
                    payload = {
                        "message": update[0],
                        "state": update[1],
                    }
                    yield (json.dumps(payload) + "\n").encode("utf-8")

            return StreamingResponse(generate_updates(), media_type="text/event-stream")

    def get_app(self):
        return self.app
