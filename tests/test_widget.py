import pytest
from src.widget import mask_info, convert_date


@pytest.mark.parametrize("x, answer", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                       ("Счет 64686473678894779589", "Счет **9589"),
                                       ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658")])
def test_mask_info(x, answer):
    assert mask_info(x) == answer


@pytest.mark.parametrize("x, answer", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_convert_date(x, answer):
    assert convert_date(x) == answer
