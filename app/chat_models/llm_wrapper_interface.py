from abc import ABC, abstractmethod

class LLMWrapper(ABC):

    def __init__(self):
        ...
    
    @abstractmethod
    def get_message(self, message, conversation_history) -> str:
        ...