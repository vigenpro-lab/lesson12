from typing import Dict, List
import pandas as pd


def read_csv_file(filename: str) -> List[Dict]:
    """Читает файл CSV и возвращает список транзакций"""
    if not filename.endswith(".csv"):
        return []

    df = pd.read_csv(filename, encoding="utf-8")
    transactions = df.to_dict(orient="records")
    return transactions


def read_xlsx_file(filename: str) -> List[Dict]:
    """Читает файл XLSX и возвращает список транзакций"""
    if not filename.endswith(".xlsx"):
        return []

    data = pd.read_excel(filename)
    return data.to_dict(orient="records")
