import logging
import os
from typing import Any, Union

import requests

logging.basicConfig(
    filename="external_api.log",  # Имя файла для логирования
    filemode="w",  # 'w' для перезаписи файла при каждом запуске
    level=logging.INFO,  # Уровень логирования
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Формат логов
)

logger = logging.getLogger(__name__)

API_KEY = os.getenv("api_keys")


def get_currency_rate(curren: str) -> Union[float, Any]:
    """Получает текущий курс валюты по отношению к рублю (RUB) с использованием внешнего API"""
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{curren}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        rate_rub = response_data["conversion_rates"]["RUB"]
        logger.info(f"Курс валюты для {curren} по отношению к RUB: {rate_rub}")
        return rate_rub
    except requests.exceptions.RequestException as ef:
        logger.error(f"Ошибка при получении обменного курса: {ef}")
        return 1.0
