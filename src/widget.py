from datetime import datetime
from src.masks import number_cart_mask, account_mask


def mask_info(input_string: str) -> str:
    """функция которая шифрует и номер карты и номер счета"""
    parts = input_string.split(" ")
    if parts[0] == "Счет":
        return f"Счет {account_mask(parts[-1])}"
    else:
        return f'{" ".join(parts[:-1])} {number_cart_mask(parts[-1])}'


def convert_date(data: str) -> str:
    """функция которая возвращет дату"""
    beta = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
    return beta.strftime('%d.%m.%Y')


