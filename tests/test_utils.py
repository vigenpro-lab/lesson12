import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.utils import read_json_file, sum_amount, transactions_rub_to_usd


class TestMyModule(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"name": "Test", "amount": 10.0}]')
    def test_read_json_file(self, mock_file: MagicMock) -> None:
        result = read_json_file("test.json")
        self.assertEqual(result, [{"name": "Test", "amount": 10.0}])

    @patch("requests.get")
    def test_transactions_rub_to_usd(self, mock_get: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_get.return_value = mock_response

        result = transactions_rub_to_usd("EUR")
        self.assertEqual(result, 75.0)

    def test_sum_amount(self) -> None:
        beta = {"operationAmount": {"currency": {"code": "RUB"}, "amount": 100.0}}
        result = sum_amount(beta)
        self.assertEqual(result, 100.0)
