import re
from pathlib import Path
from typing import Any, Dict, Iterator, List

from src.addition import filter_transactions
from src.csv_xlsx import read_csv_file, read_xlsx_file
from src.generators import card_number_generator
from src.processing import filter_state, sort_date
from src.utils import read_json_file, sum_amount
from src.widget import convert_date, mask_info


def format_open_file() -> Any:
    """Функция для открытия определённого файла"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакициями.")
    file_open = input("Выберите необходимый пункт меню: 1.JSON 2.CSV 3.Excel\n")
    if file_open == "1" or file_open.lower() == "json":
        print("Для обработки выбран json файл.")
        return read_json_file(Path("data/operations.json"))
    elif file_open == "2" or file_open.lower() == "csv":
        print("Для обработки выбран CSV файл.")
        return read_csv_file("data/transactions.csv")
    elif file_open == "3" or file_open.lower() == "excel":
        print("Для обработки выбран Excel файл.")
        return read_xlsx_file("data/transactions_excel.xlsx")
    else:
        print("Некорректный ввод, повторите ввод")
        return format_open_file()


def filter_status(data: List[Dict[Any, Any]]) -> List[Dict[Any, Any]]:
    """Функция для выбора статуса EXECUTED, CANCELED, PENDING"""
    while True:
        print("Введите статус по которому необходимо выполнить фильтрацию.")
        format_ = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
        if format_.upper() in ("EXECUTED", "CANCELED", "PENDING"):
            print(f'Операции отфильтрованы по статусу "{format_.upper()}"')
            filtered_data = filter_state(data, format_)
            print(f"Количество транзакций после фильтрации по статусу: {len(filtered_data)}")
            return filtered_data
        else:
            print(f'Статус операции "{format_}" недоступен.')


def sort_by_date(data: List[Dict[Any, Any]]) -> List[Dict[Any, Any]] | Iterator[dict]:
    """Сортирует список транзакций"""
    sort = input("Отсортировать операции по дате? Да/Нет \n")
    if sort.lower() == "да":
        while True:
            figure = input("Отсортировать по возрастанию или по убыванию? \n")
            if figure.lower() == "по возрастанию":
                sorted_data = sort_date(data)
                print("Транзакции отсортированы по возрастанию")
                return sorted_data
            elif figure.lower() == "по убыванию":
                sorted_data = sort_date(data, reverse=True)
                print("Транзакции отсортированы по убыванию")
                return sorted_data
            else:
                print("Некорректное значение, введите ещё раз")
    elif sort.lower() == "нет":
        return data
    else:
        print("Некорректный ответ, повторите ввод")
        return sort_by_date(data)


def filter_currency(data: List[Dict[Any, Any]]) -> List[Dict[Any, Any]]:
    """Фильтрация только рублевых транзакций"""
    currency_filter = input("Выводить только рублевые тразакции? Да/Нет\n")
    if currency_filter.lower() == "да":
        filtered_data = [transaction for transaction in data if transaction.get("currency") == "RUB"]
        print(f"Количество транзакций после фильтрации по валюте: {len(filtered_data)}")
        return filtered_data
    elif currency_filter.lower() == "нет":
        return data
    else:
        print("Некорректный ввод, повторите")
        return filter_currency(data)


def filter_user_keyword(data: List[Dict[Any, Any]]) -> Any:
    """Фильтрация по введённому слову"""
    keyword = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n")
    if keyword.lower() == "да":
        find_ = input("Что бы вы хотели найти?\n")
        filtered_data = filter_transactions(data, find_)
        print(f"Количество транзакций после фильтрации по ключевому слову: {len(filtered_data)}")
        return filtered_data
    elif keyword.lower() == "нет":
        return data
    else:
        print("Некорректный ввод, введите ещё раз")
        return filter_user_keyword(data)


def print_transaction(data: List[Dict[Any, Any]]) -> None:
    """Вывод отформатированного списка транзакций"""
    print("Распечатываю итоговый список транзакций")
    if data and len(data) != 0:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        descriptions_iterator = card_number_generator(start=1, finish=len(data))
        for transaction in data:
            print(convert_date(transaction["date"]), transaction["description"])
            print(next(descriptions_iterator))
            if re.search("Перевод", transaction["description"]):
                print(mask_info(transaction["from"]), "->", mask_info(transaction["to"]))
            else:
                print(mask_info(transaction["to"]))
            print(f"Сумма: {sum_amount(transaction)} руб. \n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main() -> None:
    """Функция запускающая обработку транзакций"""
    data = format_open_file()
    data = filter_status(data)
    data = sort_by_date(data)
    data = filter_currency(data)
    data = filter_user_keyword(data)
    print_transaction(data)


if __name__ == "__main__":
    main()
