import pytest
from typing import List
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency() -> None:
    """тест с одной транзакцией, ожидаемое значение: 1 транзакция"""
    transactions = [{"operationAmount": {"currency": {"code": "USD"}}}]
    beta = "USD"
    number = 1

    answer = list(filter_by_currency(transactions, beta))

    assert len(answer) == number
    assert all(transaction["operationAmount"]["currency"]["code"] == beta for transaction in answer)


def test_filter_by_currency_empty_list() -> None:
    """тест с пустым списком транзакций, ожидаемое значение: 0 транзакций"""
    transactions: List[dict] = []
    beta = "USD"
    number = 0

    answer = list(filter_by_currency(transactions, beta))

    assert len(answer) == number


@pytest.mark.parametrize("transactions, expected_descriptions", [
    ([{"description": "Перевод организации"}], ["Перевод организации"]),  # тест с одной транзакцией
    ([{"description": "Перевод со счета на счет"}, {"description": "Покупка товаров"},  # тест с тремя транзакциями
      {"description": "Списание средств"}], ["Перевод со счета на счет", "Покупка товаров", "Списание средств"]),
    ([], [])  # тест с пустым списком транзакций
])
def test_transaction_descriptions(transactions: List[dict], expected_descriptions: List[str]) -> None:
    answer = list(transaction_descriptions(transactions))
    assert answer == expected_descriptions


def test_card_number_generator() -> None:
    start = 1
    finish = 5

    expected_card_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    answer = list(card_number_generator(start, finish))

    assert answer == expected_card_numbers
