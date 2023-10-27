from abc import ABC, abstractclassmethod

class StixBuilder(ABC):
    @abstractclassmethod
    def create(self, data):
        raise NotImplementedError("The create() method must be implemented in child classes.")