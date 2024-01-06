"""
Capulet engine class.
"""


from engine.engine import Engine


class CapuletEngine(Engine):
    """
    Implement Engine interface.
    """
    def __init__(self,
                 current_mileage: int,
                 last_service_mileage: int) -> None:
        """
        Initialize an instance of CapuletEngine.

        Args:
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.
        """
        super().__init__()
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def get_current_mileage(self) -> int:
        """
        Return current mileage.

        Returns:
            int: Current mileage.
        """
        return self.__current_mileage

    def get_last_service_mileage(self) -> int:
        """
        Return the milage at last service.

        Returns:
            int: Mileage at last service.
        """
        return self.__last_service_mileage

    def needs_service(self) -> bool:
        """
        Check if engine needs service. Capulet engine needs service
        every 30000 miles.

        Returns:
            bool: True if engine needs service. False otherwise.
        """
        last = self.get_last_service_mileage()
        current = self.get_current_mileage()
        return current - last > 30000
