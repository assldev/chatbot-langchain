from chat_models.llm_wrapper_interface import LLMWrapper
from langchain_openai import OpenAI

class OpenAIWrapper(LLMWrapper):

    chatbot = None

    # CONFIG VARIABLE & THEIR DEFAULTS
    temperature = 0.5

    def __init__(self):
        self.chatbot = OpenAI(temperature=self.temperature)
    
    def set_config(self, config_obj):
        if config_obj["temperature"]:
            self.temperature = config_obj["temperature"]

    def get_message(self, message, conversation_history = []) -> str:
        return self.chatbot.invoke(message)