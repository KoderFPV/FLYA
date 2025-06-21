import os
from agents.agents import Agents
from server.server import Server
from dotenv import load_dotenv
from config.config import Config

load_dotenv()

config = Config(
    chat_model=os.getenv("CHAT_MODEL") or "",
    chat_api_key=os.getenv("CHAT_MODEL_API_KEY") or "",
)

agents = Agents(
    config.chat_model,
    config.chat_api_key
)

server = Server(
    agents=agents
)

app = server.get_app()
