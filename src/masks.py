import logging

# Настройка логирования
logging.basicConfig(
    filename="masks.log",  # Имя файла для логирования
    filemode="w",  # 'w' для перезаписи файла при каждом запуске
    level=logging.INFO,  # Уровень логирования
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Формат логов
)


def number_cart_mask(number: str) -> str:
    """функция - которая шифрует номер карты"""
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def account_mask(number: str) -> str:
    """функция - которая шифрует номер счета"""
    return f"**{number[-4:]}"
