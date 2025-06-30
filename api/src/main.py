import os
import sys
from agents.agents import Agents
from dbs.weaviate_client import WeaviateClient
from dbs.mongo_client import MongoDBClient
from server.server import Server
from dotenv import load_dotenv
from config.config import Config

load_dotenv()

new_path = "api/src"

script_dir = os.path.dirname(os.path.abspath(__file__))

absolute_new_path = os.path.join(script_dir, new_path)

print(f"Adding {absolute_new_path} to Python path.")

if absolute_new_path not in sys.path:
    sys.path.insert(0, absolute_new_path)

print("Python path configured to include /app/src.")

mongoDb = MongoDBClient(
    os.getenv("MONGO_URL") or "",
    os.getenv("MONGO_DATABASE") or "",
)
weaviateDb = WeaviateClient(
    http_host=os.getenv("WEAVIATE_HTTP_HOST") or "",
    grpc_host=os.getenv("WEAVIATE_GRPC_HOST") or "",
    api_key=os.getenv("WEAVIATE_API_KEY") or "",
)

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
