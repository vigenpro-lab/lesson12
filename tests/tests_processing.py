import pytest
from typing import List, Dict
from src.processing import filter_state, sort_date


@pytest.fixture
def data() -> List[Dict[str, str]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.mark.parametrize("x, total", [("EXECUTED", 2), ("CANCELED", 2)])
def test_filter_state(data: List[Dict[str, str]], x: str, total: int) -> None:
    result = filter_state(data, state=x)
    assert len(result) == total
    for i in result:
        assert i['state'] == x


@pytest.mark.parametrize("x, total", [("desc", True), ("asc", False)])
def test_sort_date(data: List[Dict[str, str]], x: str, total: int) -> None:
    result = sort_date(data, order=x)
    assert len(result) == 4
