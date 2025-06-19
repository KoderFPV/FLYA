import os
from agent.agent import Agent
from server.server import Server
from dotenv import load_dotenv
from config.config import Config

load_dotenv()

config = Config(
    chat_model=os.getenv("CHAT_MODEL") or "",
    chat_api_key=os.getenv("CHAT_MODEL_API_KEY") or "",
)

agent = Agent(
    config.chat_model,
    config.chat_api_key
)

server = Server(
    agent=agent
)

app = server.get_app()
