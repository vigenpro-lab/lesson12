"""функция - которая шифрует номер карты"""


def number_cart_mask(number: str) -> str:
    return f"{number[:4]} {number[5:7]}** **** {number[-4:]}"


"""функция - которая шифрует номер счета"""


def account_mask(number: str) -> str:
    return f"**{number[-4:]}"
