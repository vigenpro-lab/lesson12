import pytest

from src.masks import account_mask, number_cart_mask


@pytest.mark.parametrize(
    "x, answer",
    [("7000792289606361", "7000 79** **** 6361"), ("1234567890123456", "1234 56** **** 3456")],
)
def test_number_cart_mask(x: str, answer: str) -> None:
    assert number_cart_mask(x) == answer


@pytest.mark.parametrize("x, answer", [("73654108430135874305", "**4305"), ("1234567890123456", "**3456")])
def test_account_mask(x: str, answer: str) -> None:
    assert account_mask(x) == answer
