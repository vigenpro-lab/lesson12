import pytest
from typing import Tuple, List
from src.widget import mask_info, convert_date


@pytest.fixture
def account_data() -> Tuple[str, str]:
    return "Счет 1234567890123456", "Счет **3456"


@pytest.fixture
def card_data() -> Tuple[str, str]:
    return "Номер карты 1234 5678 9012 3456", "Номер карты 1234 5678 9012 3456 ** **** 3456"


@pytest.fixture
def date_data() -> List[Tuple[str, str]]:
    return [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2022-04-30T12:00:00.000000", "30.04.2022"),
        ("2024-04-30T00:00:00.000000", "30.04.2024")
    ]


def test_mask_info(account_data: Tuple[str, str], card_data: Tuple[str, str]) -> None:
    account_input, expected_account_output = account_data
    card_input, expected_card_output = card_data

    assert mask_info(account_input) == expected_account_output
    assert mask_info(card_input) == expected_card_output


def test_convert_date(date_data: List[Tuple[str, str]]) -> None:
    for i, j in date_data:
        assert convert_date(i) == j
