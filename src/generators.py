def filter_by_currency(transactions: list[dict], currency: str) -> list[dict]:
    """Функция, которая выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in transactions:
        try:
            currency_code = transaction["operationAmount"]["currency"]["code"]
        except KeyError:
            continue

        if currency == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) ->str:
    """Функция генератор возвращающая описание каждой операции по очереди"""
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(initial_number: int, final_number: int) -> str:
    """Функция генератор генерирующая номера банковских карт"""
    for number in range(initial_number, final_number + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
