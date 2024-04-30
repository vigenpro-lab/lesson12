def number_cart_mask(number: str) -> str:
    """функция - которая шифрует номер карты"""
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def account_mask(number: str) -> str:
    """функция - которая шифрует номер счета"""
    return f"**{number[-4:]}"
