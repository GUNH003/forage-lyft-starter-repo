"""
CarFactory combines instances of Battery, Engine and Car to create specific
types of cars.
"""


from datetime import datetime
from serviceable.car import Car
from engine import capulet_engine, willoughby_engine, sternman_engine
from battery import spindler_battery, nubbin_battery


class CarFactory:
    """
    Implement factory design pattern to create specific car model by combining
    different engine, battery and car objects.
    """
    def create_calliope(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:
        """
        Create a Calliope instance by combining a CapuletEngine object,
        a SpindlerBattery object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.

        Returns:
            Car: Calliope with a Capulet engine and a Spindler battery.
        """
        engine = capulet_engine.CapuletEngine(current_mileage,
                                              last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date,
                                                   last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:
        """
        Create a Glissade instance by combining a WilloughbyEngine object,
        a SpindlerBattery object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.

        Returns:
            Car: Glissade with a Willoughby engine and a Spindler battery.
        """
        engine = willoughby_engine.WilloughbyEngine(current_mileage,
                                                    last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date,
                                                   last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date: datetime,
                          last_service_date: datetime,
                          warning_light_on: bool) -> Car:
        """
        Create a Palindrome instance by combining a SternmanEngine object,
        a SpindlerBattery object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime):  Date of last service.
            warning_light_on (bool): Status of engine warning light.

        Returns:
            Car: Palindrome with a Sternman engine and a Spindler battery.
        """
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(current_date,
                                                   last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date: datetime,
                         last_service_date: datetime,
                         current_mileage: int,
                         last_service_mileage: int) -> Car:
        """
        Create a Rorschach instance by combining a WilloughbyEngine object,
        a NubbinBattery object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.

        Returns:
            Car: Rorschach with a Willoughby engine and a Nubbin battery.
        """
        engine = willoughby_engine.WilloughbyEngine(current_mileage,
                                                    last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date,
                                               last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date: datetime,
                      last_service_date: datetime,
                      current_mileage: int,
                      last_service_mileage: int) -> Car:
        """
        Create a Thovex instance by combining a CapuletEngine object,
        a NubbinBattery object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.

        Returns:
            Car: Thovex with a Capulet engine and a Nubbin battery.
        """
        engine = capulet_engine.CapuletEngine(current_mileage,
                                              last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date,
                                               last_service_date)
        car = Car(engine, battery)
        return car
