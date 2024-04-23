import pytest
from src.masks import number_cart_mask, account_mask


@pytest.fixture()
def tests_number_cart_mask():
    return "7000 92** **** 6361"


def test_tests_number_cart_mask(tests_number_cart_mask):
    assert tests_number_cart_mask == "7000 92** **** 6361"


def test_number_cart_mask():
    assert number_cart_mask("7000192229634351") == "7000 92** **** 4351"
    assert number_cart_mask("") == ""


@pytest.fixture()
def tests_account_mask():
    return "**4305"


def test_tests_account_mask(tests_account_mask):
    assert tests_account_mask == "**4305"


def test_account_mask():
    assert account_mask("") == ""
