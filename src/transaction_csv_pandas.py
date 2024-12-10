import logging
from typing import Any

import pandas as pd

logger = logging.getLogger("transaction_csv_pandas")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("logs/transaction_csv_pandas.log", mode="w", encoding="utf-8")
handler.setFormatter(formatter)
logger.addHandler(handler)


def read_csv(file_path: str) -> Any:
    """Функция реализует считывание файла формата CSV"""
    try:
        csv_reader = pd.read_csv(file_path, delimiter=";")
    except FileNotFoundError:
        logger.error("File not found")
        return []
    dict_reader = csv_reader.to_dict(orient="records")
    return dict_reader


def read_excel(file_path: str) -> Any:
    """Функция реализует считывание файла формата EXCEL"""
    try:
        excel_reader = pd.read_excel(file_path)
    except FileNotFoundError:
        logger.error("File not found")
        return []
    dict_reader = excel_reader.to_dict(orient="records")
    return dict_reader
