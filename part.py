from abc import ABC, abstractmethod

# abstract base class for serviceable parts
class Part(ABC):
    @abstractmethod
    def needs_service(self):
        pass