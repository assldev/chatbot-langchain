from chat_models.llm_wrapper_interface import LLMWrapper
from langchain_openai import OpenAI

class OpenAIWrapper(LLMWrapper):

    chatbot = None

    def __init__(self, _temperature):
        self.chatbot = OpenAI(temperature=_temperature)

    def get_message(self, message, conversation_history = []) -> str:
        return self.chatbot.invoke(message)