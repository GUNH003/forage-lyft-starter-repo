"""
Octoprime tire class.
"""


from tire.tire import Tire


class OctoprimeTire(Tire):
    """
    Implement Tire interface.
    """
    def __init__(self, tire_wear_array: list) -> None:
        """
        Initialize an instance of OctoprimeTire.

        Args:
            tire_wear_array (list): List of four numbers (between 0.0 and
                                    1.0 inclusive) representing how worn
                                    each of the tires are.
        """
        super().__init__()
        if len(tire_wear_array) != 4:
            raise ValueError("Tire wear array should include four\
numbers between 0.0 and 1.0 inclusive.")
        for output in tire_wear_array:
            if output < 0.0 or output > 1.0:
                raise ValueError("Tire wear array should include four\
numbers between 0.0 and 1.0 inclusive.")
        self.__tire_wear_array = tire_wear_array

    def get_tire_wear_array(self) -> list:
        """
        Return tire wear array.

        Returns:
            list: Tire wear array.
        """
        return self.__tire_wear_array

    def needs_service(self) -> bool:
        """
        Check if tires need service. Octoprime tires need service when
        the sum of all values in the tire wear array is greater than or
        equal to 3.0.

        Returns:
            bool: True if tires need service. False otherwise.
        """
        return sum(self.get_tire_wear_array()) >= 3.0
