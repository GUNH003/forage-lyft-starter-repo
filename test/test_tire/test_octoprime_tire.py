"""
Unittest for Octoprime tire.
"""


import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprime(unittest.TestCase):

    def setUp(self) -> None:
        """
        tire_wear_array_1: contain one value smaller than 0.0.
        tire_wear_array_2: contain one value greater than 1.0.
        tire_wear_array_3: contain less than four elements.
        tire_wear_array_4: contain more than four elements.
        tire_wear_array_5: contain all zeros.
        tire_wear_array_6: contain all ones.
        tire_wear_array_7: valid input, sum of all values smaller than 3.
        tire_wear_array_8: valid input, sum of all values equal to 3.
        tire_wear_array_9: valid input, sum of all values greater than 3.
        """
        self.tire_wear_array_1 = [-0.5, 0.1, 0.3, 0.9]
        self.tire_wear_array_2 = [0.5, 0.1, 0.9, 1.2]
        self.tire_wear_array_3 = [0.2, 0.4, 0.1]
        self.tire_wear_array_4 = [0.1, 0.0, 1.0, 0.4, 0.5]
        self.tire_wear_array_5 = [0.0, 0.0, 0.0, 0.0]
        self.tire_wear_array_6 = [1.0, 1.0, 1.0, 1.0]
        self.tire_wear_array_7 = [0.1, 0.3, 0.5, 0.7]
        self.tire_wear_array_8 = [0.8, 0.8, 0.7, 0.7]
        self.tire_wear_array_9 = [0.8, 0.8, 0.8, 0.8]

    def test_invalid_argument_value_smaller_than_zero(self):
        """
        Test tire should not be initialized because of invalid value in
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            OctoprimeTire(self.tire_wear_array_1)

    def test_invalid_argument_value_greater_than_one(self):
        """
        Test tire should not be initialized because of invalid value in
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            OctoprimeTire(self.tire_wear_array_2)

    def test_invalid_argument_length_smaller_than_four(self):
        """
        Test tire should not be initialized because of invalid length of
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            OctoprimeTire(self.tire_wear_array_3)

    def test_invalid_argument_length_greater_than_four(self):
        """
        Test tire should not be initialized because of invalid length of
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            OctoprimeTire(self.tire_wear_array_4)

    def test_valid_argument_all_zeros(self):
        """
        Test tire should be initialized because argument tire wear array is
        valid.
        """
        try:
            OctoprimeTire(self.tire_wear_array_5)
        except Exception:
            self.fail()

    def test_valid_argument_all_ones(self):
        """
        Test tire should be initialized because argument tire wear array is
        valid.
        """
        try:
            OctoprimeTire(self.tire_wear_array_6)
        except Exception:
            self.fail()

    def test_not_need_service_sum_smaller_than_3(self):
        """
        Test tire should not be serviced when all values in tire wear array is
        smaller than 0.9.
        """
        tire = OctoprimeTire(self.tire_wear_array_7)
        self.assertFalse(tire.needs_service())

    def test_need_service_sum_equal_to_3(self):
        """
        Test tire should be serviced when one value in tire wear array is
        equal to 0.9.
        """
        tire = OctoprimeTire(self.tire_wear_array_8)
        self.assertTrue(tire.needs_service())

    def test_need_service_sum_greater_than_3(self):
        """
        Test tire should be serviced when one value in tire wear array is
        greater than 0.9.
        """
        tire = OctoprimeTire(self.tire_wear_array_9)
        self.assertTrue(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
