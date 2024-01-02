from abc import ABC, abstractmethod

class StixBuilder(ABC):
    @abstractmethod
    def create(self):
        raise NotImplementedError("The create() method must be implemented in child classes.")