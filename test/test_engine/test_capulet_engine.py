"""
Unittest for Capulet engine.
"""


import unittest
from engine.capulet_engine import CapuletEngine


class TestCapulet(unittest.TestCase):

    def setUp(self) -> None:
        """
        last_service_mileage: 0 miles.
        current_mileage_1: 29999 miles.
        current_mileage_2: 30000 miles.
        current_mileage_3: 30001 miles.
        """
        self.last_service_mileage = 0
        self.current_mileage_1 = 29999
        self.current_mileage_2 = 30000
        self.current_mileage_3 = 30001

    def test_not_need_service_after_29999_miles(self):
        """
        Test engine should not be serviced after 29999 miles.
        """
        engine = CapuletEngine(self.current_mileage_1,
                               self.last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_not_need_service_after_30000_miles(self):
        """
        Test engine should not be serviced after 30000 miles.
        """
        engine = CapuletEngine(self.current_mileage_2,
                               self.last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_need_service_after_30001_miles(self):
        """
        Test engine should be serviced after 30001 miles.
        """
        engine = CapuletEngine(self.current_mileage_3,
                               self.last_service_mileage)
        self.assertTrue(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
