"""
Interface for all serviceables.
"""


from abc import ABC, abstractmethod


class Serviceable(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass
