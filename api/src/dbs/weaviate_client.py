import weaviate
from weaviate.classes.init import Auth


class WeaviateClient:
    def __init__(self, http_host: str, grpc_host: str, api_key: str,
                 http_port: int = 443, http_secure: bool = True,
                 grpc_port: int = 443, grpc_secure: bool = True):
        self._client = None
        self._http_host = http_host
        self._grpc_host = grpc_host
        self._api_key = api_key
        self._http_port = http_port
        self._http_secure = http_secure
        self._grpc_port = grpc_port
        self._grpc_secure = grpc_secure
        self._connect()

    def _connect(self):
        try:
            auth_credentials = None
            if self._api_key:
                auth_credentials = Auth.api_key(self._api_key)

            self._client = weaviate.connect_to_custom(
                http_host=self._http_host,
                http_port=self._http_port,
                http_secure=self._http_secure,
                grpc_host=self._grpc_host,
                grpc_port=self._grpc_port,
                grpc_secure=self._grpc_secure,
                auth_credentials=auth_credentials,
            )

            if not self._client.is_ready():
                raise ConnectionError(
                    "Weaviate client is not ready after connection attempt.")

            print(
                "Successfully connected to Weaviate. "
                f"HTTP Host: {self._http_host}, gRPC Host: {self._grpc_host}"
            )
        except ConnectionError as e:
            print(f"Weaviate connection error: {e}")
            self._client = None
        except Exception as e:
            print(
                f"An unexpected error occurred during Weaviate connection: {e}")
            self._client = None

    def get_client(self) -> weaviate.WeaviateClient:
        if self._client:
            return self._client
        else:
            raise ConnectionError(
                "Weaviate client is not connected.")

    def close_connection(self):
        if self._client:
            self._client.close()
            print("Weaviate connection closed.")
            self._client = None
