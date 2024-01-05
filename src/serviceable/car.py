"""
Car class.
"""


from serviceable.serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery


class Car(Serviceable):
    """
    Implement Serviceable interface.
    """
    def __init__(self, engine: Engine, battery: Battery) -> None:
        """
        Initialize a Car instance.

        Args:
            engine (Engine): Engine of the Car instance.
            battery (Battery): Battery of the Car instance.
        """
        super().__init__()
        self.__engine = engine
        self.__battery = battery

    def get_engine(self) -> Engine:
        """
        Return car engine.

        Returns:
            Engine: Car engine.
        """
        return self.__engine

    def get_battery(self) -> Battery:
        """
        Return car battery.

        Returns:
            Battery: Car battery.
        """
        return self.__battery

    def needs_service(self) -> bool:
        """
        Go through each component of the Car instance to check
        if service is needed.

        Returns:
            bool: True if at least one car part needs service.
                  False otherwise.
        """
        for item in vars(self).items():
            if item[1].needs_service():
                return True
        return False
