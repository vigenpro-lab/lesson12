import unittest
from unittest.mock import patch, mock_open, MagicMock
from src.utils import read_json_file, transactions_rub_to_usd, sum_amount


class TestMyModule(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"name": "Test", "amount": 10.0}]')
    def test_read_json_file(self, mock_file):
        result = read_json_file("test.json")
        self.assertEqual(result, [{"name": "Test", "amount": 10.0}])

    @patch("requests.get")
    def test_transactions_rub_to_usd(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_get.return_value = mock_response

        result = transactions_rub_to_usd("EUR")
        self.assertEqual(result, 75.0)

    def test_sum_amount(self):
        beta = {"operationAmount": {"currency": {"code": "RUB"}, "amount": 100.0}}
        result = sum_amount(beta)
        self.assertEqual(result, 100.0)
