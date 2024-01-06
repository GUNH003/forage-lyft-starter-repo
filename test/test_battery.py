"""
Unittest for batteries.
"""


import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestSpindler(unittest.TestCase):

    def setUp(self) -> None:
        """
        last_service_date_1: 1 year ago.
        last_service_date_2: 2 years ago.
        last_service_date_3: 3 years ago.
        """
        self.today = datetime.today().date()
        self.last_service_date_1 = self.today.replace(year=self.today.year - 1)
        self.last_service_date_2 = self.today.replace(year=self.today.year - 2)
        self.last_service_date_3 = self.today.replace(year=self.today.year - 3)

    def test_not_need_service_after_1_year(self):
        """
        Test battery should not be serviced after 1 year.
        """
        battery = SpindlerBattery(self.today, self.last_service_date_1)
        self.assertFalse(battery.needs_service())

    def test_not_need_service_after_2_years(self):
        """
        Test battery should not be serviced after 2 years.
        """
        battery = SpindlerBattery(self.today, self.last_service_date_2)
        self.assertFalse(battery.needs_service())

    def test_need_service_after_3_years(self):
        """
        Test battery should be serviced after 3 years.
        """
        battery = SpindlerBattery(self.today, self.last_service_date_3)
        self.assertTrue(battery.needs_service())


class TestNubbin(unittest.TestCase):

    def setUp(self) -> None:
        """
        last_service_date_3: 3 years ago.
        last_service_date_4: 4 years ago.
        last_service_date_5: 5 years ago.
        """
        self.today = datetime.today().date()
        self.last_service_date_3 = self.today.replace(year=self.today.year - 3)
        self.last_service_date_4 = self.today.replace(year=self.today.year - 4)
        self.last_service_date_5 = self.today.replace(year=self.today.year - 5)

    def test_not_need_service_after_3_years(self):
        """
        Test battery should not be serviced after 3 years.
        """
        battery = NubbinBattery(self.today, self.last_service_date_3)
        self.assertFalse(battery.needs_service())

    def test_not_need_service_after_4_years(self):
        """
        Test battery should not be serviced after 4 years.
        """
        battery = NubbinBattery(self.today, self.last_service_date_4)
        self.assertFalse(battery.needs_service())

    def test_need_service_after_5_years(self):
        """
        Test battery should be serviced after 5 years.
        """
        battery = NubbinBattery(self.today, self.last_service_date_5)
        self.assertTrue(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
