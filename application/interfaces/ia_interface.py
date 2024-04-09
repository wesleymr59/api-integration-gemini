from abc import ABC, abstractmethod

class IaInterface(ABC):
    @abstractmethod
    def sendMessage(self, msg: str):
        pass