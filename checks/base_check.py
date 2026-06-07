from abc import ABC, abstractmethod

class BaseCheck(ABC):

    @abstractmethod
    def run(self, response):
        pass