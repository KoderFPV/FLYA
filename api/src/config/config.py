from dataclasses import dataclass


@dataclass
class Config:
    chat_model: str
    chat_api_key: str

    def __post_init__(self):
        if not self.chat_model:
            raise ValueError(
                "Please set the CHAT_MODEL environment variable with your chat model."
            )
        if not self.chat_api_key:
            raise ValueError(
                "Please set the CHAT_API_KEY environment variable with your Google API key."
            )
