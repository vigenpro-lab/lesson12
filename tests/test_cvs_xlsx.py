from typing import Dict, List
from unittest.mock import patch

import pandas as pd

from src.csv_xlsx import read_csv_file, read_xlsx_file


def test_read_csv_file() -> None:
    # Подготовка mock-данных
    mock_data = pd.DataFrame(
        {"date": ["2023-01-01", "2023-01-02"], "amount": [100, 200], "description": ["Deposit", "Withdrawal"]}
    )

    with patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value = mock_data

        # Вызов тестируемой функции
        result: List[Dict[str, str]] = read_csv_file("dummy.csv")

        # Ожидаемый результат
        expected: List[Dict[str, str]] = [
            {"date": "2023-01-01", "amount": 100, "description": "Deposit"},
            {"date": "2023-01-02", "amount": 200, "description": "Withdrawal"},
        ]

        # Проверка результата
        assert result == expected
        mock_read_csv.assert_called_once_with("dummy.csv", encoding="utf-8")


def test_read_xlsx_file() -> None:
    # Подготовка mock-данных
    mock_data = pd.DataFrame(
        {"date": ["2023-01-01", "2023-01-02"], "amount": [100, 200], "description": ["Deposit", "Withdrawal"]}
    )

    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = mock_data

        # Вызов тестируемой функции
        result: List[Dict[str, str]] = read_xlsx_file("dummy.xlsx")

        # Ожидаемый результат
        expected: List[Dict[str, str]] = [
            {"date": "2023-01-01", "amount": 100, "description": "Deposit"},
            {"date": "2023-01-02", "amount": 200, "description": "Withdrawal"},
        ]

        # Проверка результата
        assert result == expected
        mock_read_excel.assert_called_once_with("dummy.xlsx")
