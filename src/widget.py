from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_ifo: str) -> str:
    '''Функция принимает на вход номер счета или карты с назвванием и возвращает название и замаскированый номер'''
    parts = card_ifo.rsplit(" ", 1)
    if len(parts) < 2:
        return "Некоректный ввод"
    card_name = parts[0]
    card_number = parts[1]
    if len(card_number) == 16:
        return f"{card_name} {get_mask_card_number(card_number)}"
    elif len(card_number) == 20:
        return f"{card_name} {get_mask_account(card_number)}"
    else:
        return "Неверный номер карты или счета"


def get_date(date_info: str) -> str:
    '''Функция принимает на вход дату в формате год-месяц-дату и время и возвращает дату в формате ДД.ММ.ГГГГ'''
    date_obj = datetime.strptime(date_info, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
