"""
Sternman engine class.
"""

from engine.engine import Engine


class SternmanEngine(Engine):
    """
    Implement Engine interface.
    """
    def __init__(self, warning_light_is_on: bool) -> None:
        """
        Initialize an instance of SternmanEngine.

        Args:
            warning_light_is_on (bool): True if warning light is on.
                                        False otherwise.
        """
        super().__init__()
        self.__warning_light_is_on = warning_light_is_on

    def get_warning_light_is_on(self) -> bool:
        """
        Return warning light status.

        Returns:
            bool:  True if warning light is on. False otherwise.
        """
        return self.__warning_light_is_on

    def needs_service(self) -> bool:
        """
        Check if engine needs service. Sternman engine needs service
        when the engine warning light is on.

        Returns:
            bool: True if engine needs service. False otherwise.
        """
        return self.get_warning_light_is_on()
