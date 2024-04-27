from datetime import datetime
from typing import Any, Dict, List, Literal

data_for_filter_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

data_for_sort_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """функция для фильтра словарей по state"""
    answer = []
    for i in data:
        if i.get("state") == state:
            answer.append(i)
    return answer


# print(filter_state(data_for_filter_state))  # выводит словари где state = EXECUTED

# print(filter_state(data_for_filter_state, 'CANCELED'))  # выводит словари где state = CANCELED


def sort_date(data: List[Dict[str, Any]], order: Literal["desc", "asc"] = "desc") -> List[Dict[str, Any]]:
    """функция для сортировки словарей по дате, desc означает "по убыванию"""

    def get_dict(item: Dict[str, Any]) -> datetime:
        """функция примнимает словарь и возвращает объект даты. Для того чтоб-
        -потом использовать функцию в качесиве ключа сотрировки"""
        return datetime.fromisoformat(item["date"])

    if order == "desc":
        answer = sorted(data, key=get_dict, reverse=True)
    else:
        answer = sorted(data, key=get_dict)
    return answer

# print(sort_date(data_for_sort_date, input()))  # выводит новые отсортированные словари по дате
