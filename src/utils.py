import json
import os
import requests
from typing import Any, Dict, List, Union

API_KEY = os.getenv("api_keys")


def read_json_file(fp: str) -> List[Dict[str, Union[str, float]]]:
    try:
        with open(fp, 'r') as file:
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
    url = f"https://v6.exchangerate-api.com/v6/92038b02fd9e7e1c6b8b993d/latest/USD={curren}"
    head = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=head, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        return response_data["rates"]["RUB"]
    except requests.exceptions.RequestException as ef:
        return 1.0


def sum_amount(beta: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    # answer = 0.0
    sum = beta.get("operationAmount", {})
    # code = sum.get("currency", {}).get("code", "")
    amount = float(sum.get("amount", 0.0))
    # if code in ["USD", "EUR"]:
    #     rate_rub = transactions_rub_to_usd(code)
    #     answer += amount * rate_rub
    # elif code == "RUB":
    #     answer += amount

    return amount


beta = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

print(sum_amount(beta))
