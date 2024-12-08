import json
import logging
import os
from typing import Any

from src.external_api import get_currency

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operation_transaction(file_path):
    """Обработка JSON файла"""
    if not os.path.isfile(file_path):
        logging.error("Ошибка поиска файла")
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logging.info("Обработка данных Json-файла прошла успешно")
                return data
        except json.decoder.JSONDecodeError:
            logging.error("Ошибка декодирования")
            return []


def transactions_sum(func: Any) -> float:
    """Функция возвращает сумму транзакции в рублях"""
    datas = func
    data_str = []
    amount = []
    for trans in datas:
        if trans["operationAmount"]["currency"]["code"] == "":
            logging.info("В данных есть транзакции без указания валюты")
            continue
        elif trans["operationAmount"]["currency"]["code"] == "RUB":
            data_str.append(trans["operationAmount"]["amount"])
        elif trans["operationAmount"]["currency"]["code"] != "RUB":
            get_currency("RUB", trans["operationAmount"]["currency"]["code"], trans["operationAmount"]["amount"])
            data_str.append(trans["operationAmount"]["amount"])
    for d in data_str:
        amount.append(float(d))
    result_amount = round(float(sum(amount)), 2)
    logging.info("Сумма транзакций получена")
    return result_amount
