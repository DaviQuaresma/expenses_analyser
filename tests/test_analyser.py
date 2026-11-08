import unittest
from src.analyser import bigger_value


class TestValidator(unittest.TestCase):

    def test_bigger_value(self):

        raw_data: dict = {
            "Alimentação": 803.60,
            "Transporte": 160.00,
            "Saude": 1444.50,
            "Moradia": 660.00,
        }

        expect_result: dict = {"categoria": "Saude", "valor": 1444.50}

        result = bigger_value(raw_data)
        self.assertEqual(result, expect_result)
