from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass