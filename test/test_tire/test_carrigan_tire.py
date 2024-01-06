"""
Unittest for Carrigan tire.
"""


import unittest
from tire.carrigan_tire import CarriganTire


class TestCarrigan(unittest.TestCase):

    def setUp(self) -> None:
        """
        tire_wear_array_1: contain one value smaller than 0.0.
        tire_wear_array_2: contain one value greater than 1.0.
        tire_wear_array_3: contain less than four elements.
        tire_wear_array_4: contain more than four elements.
        tire_wear_array_5: contain all zeros.
        tire_wear_array_6: contain all ones.
        tire_wear_array_7: valid input, all values smaller than 0.9.
        tire_wear_array_8: valid input, one value equals to 0.9.
        tire_wear_array_9: valid input, one value greater than 0.9.
        tire_wear_array_10: valid input, all values equal to 0.9.
        """
        self.tire_wear_array_1 = [-0.5, 0.1, 0.3, 0.9]
        self.tire_wear_array_2 = [0.5, 0.1, 0.9, 1.2]
        self.tire_wear_array_3 = [0.2, 0.4, 0.1]
        self.tire_wear_array_4 = [0.1, 0.0, 1.0, 0.4, 0.5]
        self.tire_wear_array_5 = [0.0, 0.0, 0.0, 0.0]
        self.tire_wear_array_6 = [1.0, 1.0, 1.0, 1.0]
        self.tire_wear_array_7 = [0.1, 0.3, 0.5, 0.7]
        self.tire_wear_array_8 = [0.1, 0.3, 0.5, 0.9]
        self.tire_wear_array_9 = [0.1, 0.3, 0.5, 1.0]
        self.tire_wear_array_10 = [0.9, 0.9, 0.9, 0.9]

    def test_invalid_argument_value_smaller_than_zero(self):
        """
        Test tire should not be initialized because of invalid value in
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            CarriganTire(self.tire_wear_array_1)

    def test_invalid_argument_value_greater_than_one(self):
        """
        Test tire should not be initialized because of invalid value in
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            CarriganTire(self.tire_wear_array_2)

    def test_invalid_argument_length_smaller_than_four(self):
        """
        Test tire should not be initialized because of invalid length of
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            CarriganTire(self.tire_wear_array_3)

    def test_invalid_argument_length_greater_than_four(self):
        """
        Test tire should not be initialized because of invalid length of
        the tire wear array.
        """
        with self.assertRaises(ValueError):
            CarriganTire(self.tire_wear_array_4)

    def test_valid_argument_all_zeros(self):
        """
        Test tire should be initialized because argument tire wear array is
        valid.
        """
        try:
            CarriganTire(self.tire_wear_array_5)
        except Exception:
            self.fail()

    def test_valid_argument_all_ones(self):
        """
        Test tire should be initialized because argument tire wear array is
        valid.
        """
        try:
            CarriganTire(self.tire_wear_array_6)
        except Exception:
            self.fail()

    def test_not_need_service_all_values_smaller_than_0_9(self):
        """
        Test tire should not be serviced when all values in tire wear array is
        smaller than 0.9.
        """
        tire = CarriganTire(self.tire_wear_array_7)
        self.assertFalse(tire.needs_service())

    def test_need_service_one_value_equal_to_0_9(self):
        """
        Test tire should be serviced when one value in tire wear array is
        equal to 0.9.
        """
        tire = CarriganTire(self.tire_wear_array_8)
        self.assertTrue(tire.needs_service())

    def test_need_service_one_value_greater_than_0_9(self):
        """
        Test tire should be serviced when one value in tire wear array is
        greater than 0.9.
        """
        tire = CarriganTire(self.tire_wear_array_9)
        self.assertTrue(tire.needs_service())

    def test_need_service_all_values_equal_to_0_9(self):
        """
        Test tire should be serviced when all values in tire wear array are
        equal to 0.9.
        """
        tire = CarriganTire(self.tire_wear_array_10)
        self.assertTrue(tire.needs_service())

    def test_need_service_all_values_greater_than_0_9(self):
        """
        Test tire should be serviced when all values in tire wear array are
        greater than 0.9.
        """
        tire = CarriganTire(self.tire_wear_array_6)
        self.assertTrue(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
