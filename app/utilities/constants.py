from dataclasses import dataclass

@dataclass
class Models:
    OPENAI: str = "openai"

@dataclass
class OpenAIConfigs:
    TEMPERATURE: str = "temperature"

@dataclass
class ModelConfigs:
    OPENAI = OpenAIConfigs()

@dataclass
class Errors:
    CONFIG_KEY_NOT_FOUND: str = "CONFIG_KEY_NOT_FOUND"
    CHAT_MODEL_NOT_AVAILABLE: str = "CHAT_MODEL_NOT_AVAILABLE"
    FILE_NOT_FOUND: str = "FILE_NOT_FOUND"
    JSON_DECODE_ERROR: str = "JSON_DECODE_ERROR"