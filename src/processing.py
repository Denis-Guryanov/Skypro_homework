from datetime import datetime

from src.widget import get_date


def filter_by_state(list_on_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state, и возвращает новый список
    словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""

    filter_states = []

    for i in list_on_state:
        if i.get("state") == state:
            filter_states.append(i)

    return filter_states


def sort_by_date(list_on_date: list[dict], reverse: bool = True) -> list[dict]:
    """функция принимает список словарей и необязательный параметр, задающий порядок сортировки и
     возвращает список отвортированный по дате"""
    date_items = []

    for date in list_on_date:
        formatted_date = get_date(date["date"])
        date_object = datetime.strptime(formatted_date, "%d.%m.%Y")
        date_items.append((date_object, date))

    date_items.sort(key=lambda x: x[0], reverse=reverse)

    sorted_data = []

    for date_object, item in date_items:
        sorted_data.append(item)

    return sorted_data
