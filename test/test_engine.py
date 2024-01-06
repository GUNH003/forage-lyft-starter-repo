"""
Unittest for engines.
"""


import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


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


class TestSternman(unittest.TestCase):

    def setUp(self) -> None:
        """
        warning_light_is_on_1: warning light is off.
        warning_light_is_on_2: warning light is on.
        """
        self.warning_light_is_on_1 = False
        self.warning_light_is_on_2 = True

    def test_not_need_service_with_warning_light_off(self):
        """
        Test engine should not be serviced when warning light is off.
        """
        engine = SternmanEngine(self.warning_light_is_on_1)
        self.assertFalse(engine.needs_service())

    def test_need_service_with_warning_light_on(self):
        """
        Test engine should be serviced when warning light is on.
        """
        engine = SternmanEngine(self.warning_light_is_on_2)
        self.assertTrue(engine.needs_service())


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
