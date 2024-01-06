"""
Nubbin battery class.
"""


from datetime import datetime
from battery.battery import Battery


class NubbinBattery(Battery):
    """
    Implement Battery interface.
    """
    def __init__(self,
                 current_date: datetime,
                 last_service_date: datetime) -> None:
        """
        Initialize an instance of NubbinBattery.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
        """
        super().__init__()
        self.__current_date = current_date
        self.__last_service_date = last_service_date

    def get_current_date(self) -> datetime:
        """
        Return current date.

        Returns:
            datetime: Current date.
        """
        return self.__current_date

    def get_last_service_date(self) -> datetime:
        """
        Return date of last service.

        Returns:
            datetime: Date of last service.
        """
        return self.__last_service_date

    def needs_service(self) -> bool:
        """
        Check if battery needs service. Nubbin battery needs service
        every 2 years.

        Returns:
            bool: True if battery needs service. False otherwise.
        """
        last_service_date = self.get_last_service_date()
        service_threshold_date = last_service_date.replace(
            year=last_service_date.year + 4)
        return service_threshold_date < self.get_current_date()
