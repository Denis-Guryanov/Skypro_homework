import re
from collections import Counter
from typing import Any
def search_description(bank_operations: list[dict], for_search: str) -> list[dict]:
    """Функция, выполняющая заданный поиск в банковских операциях."""
    result_operations = []
    for element in bank_operations:
        if re.findall(for_search, element.get("description"), flags=re.IGNORECASE):
            result_operations.append(element)
        else:
            result_operations = []
    return result_operations


def count_operations(bank_operations: list[dict]) -> Any:
    """Функция, осуществляющая подсчёт количества операций по категориям."""
    category = []
    for bank_transaction in bank_operations:
        category.append(bank_transaction.get("description", {}))
    counted_category = Counter(category)
    return counted_category

