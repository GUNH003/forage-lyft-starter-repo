"""
CarFactory combines instances of Battery, Engine , Tire and Car to create
specific types of cars.
"""


from datetime import datetime
from serviceable.car import Car
from engine import capulet_engine, willoughby_engine, sternman_engine
from battery import spindler_battery, nubbin_battery
from tire import carrigan_tire, octoprime_tire


class CarFactory:
    """
    Implement factory design pattern to create specific car model by combining
    different engine, battery and car objects.
    """
    def create_calliope(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int,
                        tire_wear_array: list) -> Car:
        """
        Create a Calliope instance by combining a CapuletEngine object,
        a SpindlerBattery object and a CarriganTire object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.
            tire_wear_array (list): List of four numbers (between 0.0 and
                                    1.0 inclusive) representing how worn
                                    each of the tires are.

        Returns:
            Car: Calliope with a Capulet engine, a Spindler battery and
                 Carrigan tires.
        """
        engine = capulet_engine.CapuletEngine(current_mileage,
                                              last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date,
                                                   last_service_date)
        tire = carrigan_tire.CarriganTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car

    def create_glissade(current_date: datetime,
                        last_service_date: datetime,
                        current_mileage: int,
                        last_service_mileage: int,
                        tire_wear_array: list) -> Car:
        """
        Create a Glissade instance by combining a WilloughbyEngine object,
        a SpindlerBattery object and an OctoprimeTire object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.
            tire_wear_array (list): List of four numbers (between 0.0 and
                                    1.0 inclusive) representing how worn
                                    each of the tires are.

        Returns:
            Car: Glissade with a Willoughby engine, a Spindler battery and
                 Octoprime tires.
        """
        engine = willoughby_engine.WilloughbyEngine(current_mileage,
                                                    last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date,
                                                   last_service_date)
        tire = octoprime_tire.OctoprimeTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car

    def create_palindrome(current_date: datetime,
                          last_service_date: datetime,
                          warning_light_on: bool,
                          tire_wear_array: int) -> Car:
        """
        Create a Calliope instance by combining a SternmanEngine object,
        a SpindlerBattery object and a CarriganTire object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.
            tire_wear_array (list): List of four numbers (between 0.0 and
                                    1.0 inclusive) representing how worn
                                    each of the tires are.

        Returns:
            Car: Calliope with a Sternman engine, a Spindler battery and
                 Carrigan tires.
        """
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(current_date,
                                                   last_service_date)
        tire = carrigan_tire.CarriganTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car

    def create_rorschach(current_date: datetime,
                         last_service_date: datetime,
                         current_mileage: int,
                         last_service_mileage: int,
                         tire_wear_array: int) -> Car:
        """
        Create a Rorschach instance by combining a WilloughbyEngine object,
        a NubbinBattery object and an OctoprimeTire object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.
            tire_wear_array (list): List of four numbers (between 0.0 and
                                    1.0 inclusive) representing how worn
                                    each of the tires are.

        Returns:
            Car: Rorschach with a Willoughby engine, a Nubbin battery and
                 Octoprime tires.
        """
        engine = willoughby_engine.WilloughbyEngine(current_mileage,
                                                    last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date,
                                               last_service_date)
        tire = octoprime_tire.OctoprimeTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car

    def create_thovex(current_date: datetime,
                      last_service_date: datetime,
                      current_mileage: int,
                      last_service_mileage: int,
                      tire_wear_array: int) -> Car:
        """
        Create a Thovex instance by combining a CapuletEngine object,
        a NubbinBattery object and a CarriganTire object with a Car object.

        Args:
            current_date (datetime): Current date.
            last_service_date (datetime): Date of last service.
            current_mileage (int): Current mileage.
            last_service_mileage (int): Mileage at last service.
            tire_wear_array (list): List of four numbers (between 0.0 and
                                    1.0 inclusive) representing how worn
                                    each of the tires are.

        Returns:
            Car: Thovex with a Capulet engine, a Nubbin battery and
                 Carrigan tires.
        """
        engine = capulet_engine.CapuletEngine(current_mileage,
                                              last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date,
                                               last_service_date)
        tire = carrigan_tire.CarriganTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car
