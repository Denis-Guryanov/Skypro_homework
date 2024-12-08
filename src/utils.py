import os

import json

from typing import Any

from src.external_api import get_currency


def get_operation_transaction(file_path):
    '''Обработка JSON файла'''
    if not os.path.isfile(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
        except json.decoder.JSONDecodeError:
            print("Ошибка декодирования")
            return []


def transactions_sum(func: Any) -> float:
    """Функция возвращает сумму транзакции в рублях"""
    datas = func
    data_str = []
    amount = []
    for trans in datas:
        if trans["operationAmount"]["currency"]["code"] == "":
            continue
        elif trans["operationAmount"]["currency"]["code"] == "RUB":
            data_str.append(trans["operationAmount"]["amount"])
        elif trans["operationAmount"]["currency"]["code"] != "RUB":
            get_currency("RUB", trans["operationAmount"]["currency"]["code"], trans["operationAmount"]["amount"])
            data_str.append(trans["operationAmount"]["amount"])
    for d in data_str:
        amount.append(float(d))
    result_amount = round(float(sum(amount)), 2)
    return result_amount



