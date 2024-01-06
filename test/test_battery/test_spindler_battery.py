"""
Unittest for Spindler battery.
"""


import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery


class TestSpindler(unittest.TestCase):

    def setUp(self) -> None:
        """
        last_service_date_1: 2 year ago.
        last_service_date_2: 3 years ago.
        last_service_date_3: 4 years ago.
        """
        self.today = datetime.today().date()
        self.last_service_date_1 = self.today.replace(year=self.today.year - 2)
        self.last_service_date_2 = self.today.replace(year=self.today.year - 3)
        self.last_service_date_3 = self.today.replace(year=self.today.year - 4)

    def test_not_need_service_after_2_years(self):
        """
        Test battery should not be serviced after 2 years.
        """
        battery = SpindlerBattery(self.today, self.last_service_date_1)
        self.assertFalse(battery.needs_service())

    def test_not_need_service_after_3_years(self):
        """
        Test battery should not be serviced after 3 years.
        """
        battery = SpindlerBattery(self.today, self.last_service_date_2)
        self.assertFalse(battery.needs_service())

    def test_need_service_after_4_years(self):
        """
        Test battery should be serviced after 4 years.
        """
        battery = SpindlerBattery(self.today, self.last_service_date_3)
        self.assertTrue(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
