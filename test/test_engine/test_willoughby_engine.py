"""
Unittest for Willoughby engine.
"""


import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughby(unittest.TestCase):
    def setUp(self) -> None:
        """
        last_service_mileage: 0 miles.
        current_mileage_1: 59999 miles.
        current_mileage_2: 60000 miles.
        current_mileage_3: 60001 miles.
        """
        self.last_service_mileage = 0
        self.current_mileage_1 = 59999
        self.current_mileage_2 = 60000
        self.current_mileage_3 = 60001

    def test_not_need_service_after_59999_miles(self):
        """
        Test engine should not be serviced after 59999 miles.
        """
        engine = WilloughbyEngine(self.current_mileage_1,
                                  self.last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_not_need_service_after_60000_miles(self):
        """
        Test engine should not be serviced after 60000 miles.
        """
        engine = WilloughbyEngine(self.current_mileage_2,
                                  self.last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_need_service_after_60001_miles(self):
        """
        Test engine should be serviced after 60001 miles.
        """
        engine = WilloughbyEngine(self.current_mileage_3,
                                  self.last_service_mileage)
        self.assertTrue(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
