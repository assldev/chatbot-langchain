from utilities.constants import Models, Errors
from chat_models.openai_wrapper import OpenAIWrapper
from chat_models.huggingface_wrapper import HuggingFaceWrapper

class LLMFactory:
    
    factory_obj = None

    def __new__(self):
        if self.factory_obj is None:
            self.factory_obj = super().__new__(self)
        return self.factory_obj
    
    def get_llm(self, model_name: str, model_config={}):
        if model_name == Models.OPENAI:
            chatbot = OpenAIWrapper()
            chatbot.set_config(model_config)
            return chatbot
        else:
            raise Exception(f"{Errors.CHAT_MODEL_NOT_AVAILABLE}: {model_name}")
