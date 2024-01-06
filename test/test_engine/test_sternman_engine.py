"""
Unittest for Sternman engine.
"""


import unittest
from engine.sternman_engine import SternmanEngine


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


if __name__ == "__main__":
    unittest.main()
