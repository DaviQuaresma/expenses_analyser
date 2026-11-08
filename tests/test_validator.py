import unittest
from src.validator import changeDate, changeMoney
import datetime as dt
from decimal import Decimal as dc

class TestValidator(unittest.TestCase):

    def test_if_return_valid_format_date(self):
        date: str = "2025-08-22"
        expect_date = dt.datetime.strptime(date, "%Y-%m-%d").date()
        result = changeDate(date)
        
        self.assertEqual(result, expect_date)

    def test_if_return_valid_money(self):
        money: str = "250,50"
        expect_money = dc(money.replace(",", "."))
        result = changeMoney(money)
        
        self.assertEqual(result, expect_money)