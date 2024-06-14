import json
import logging
import os
from typing import Any, Dict, List, Union

import requests

logging.basicConfig(
    filename="utils.log",  # Имя файла для логирования
    filemode="w",  # 'w' для перезаписи файла при каждом запуске
    level=logging.INFO,  # Уровень логирования
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Формат логов
)

logger = logging.getLogger(__name__)

API_KEY = os.getenv("api_keys")


def read_json_file(fp: str) -> List[Dict[str, Union[str, float]]]:
    """Читает JSON файл и возвращает данные в виде списка словарей"""
    try:
        with open(fp, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print("File not found")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return []


def transactions_rub_to_usd(curren: str) -> Union[float, Any]:
    """Получает текущий курс валюты по отношению к рублю (RUB) с использованием внешнего API"""
    url = f"https://v6.exchangerate-api.com/v6/92038b02fd9e7e1c6b8b993d/latest/USD={curren}"
    head = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=head, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        return response_data["rates"]["RUB"]
    except requests.exceptions.RequestException as ef:
        print(f"Ошибка при получении обменного курса: {ef}")
        return 1.0


def sum_amount(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли, если валюта не является USD или EUR"""
    """Возвращает сумму транзакции в рублях."""
    operation_amount = transaction.get("operationAmount", {})
    currency_code = operation_amount.get("currency", {}).get("code", "")
    amount = float(operation_amount.get("amount", 0.0))

    if currency_code not in ["USD", "EUR"]:
        rate_rub = transactions_rub_to_usd(currency_code)
        amount *= rate_rub

    return amount


data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
