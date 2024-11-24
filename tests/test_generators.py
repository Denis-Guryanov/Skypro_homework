import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def test_filter_by_currency_currency(trans_list, currency):
    for trans in trans_list:
        assert filter_by_currency(trans.get("operationAmount").get("currency").get("name")) == currency


def test_filter_by_currency_without_currency_code():
    """
    Если в транзакции отсутствует код транзакции,
    то она не учитывается при фильтрации.
    """
    transaction_without_currency_code = _create_transaction(1, 'USD')
    transaction_without_currency_code['operationAmount']['currency'].pop('code')

    gen = filter_by_currency([transaction_without_currency_code], 'USD')

    assert list(gen) == []


def test_filter_by_currency_returns_only_transactions_with_specified_currency_code():
    """
    Возвращаются только транзации с указанным кодом валюты.
    """
    rub_transactions = [
        _create_transaction(1, "RUB"), _create_transaction(2, "RUB")
    ]
    usd_transactions = [
        _create_transaction(3, "USD"), _create_transaction(4, "USD")
    ]
    aed_transactions = [
        _create_transaction(5, "AED"), _create_transaction(6, "AED")
    ]
    transactions = [*rub_transactions, *usd_transactions, *aed_transactions]

    gen = filter_by_currency(transactions, 'USD')

    assert list(gen) == usd_transactions


def test_filter_by_currency_no_transactions():
    """
    Если передать пустой список транзакций, то вернется пустой список.
    """
    gen = filter_by_currency([], 'USD')
    assert list(gen) == []


def _create_transaction(transaction_id: int, currency_code: str) -> dict:
    return {
        "id": transaction_id,
        "operationAmount": {"amount": "100.0", "currency": {"name": "руб.", "code": currency_code}},
    }


@pytest.mark.parametrize("transactions, expected", [
    ([], []),
    ([{"description": "Перевод"}, {"description": "Покупка"}], ["Перевод", "Покупка"]),
    ([{"description": "Снятие наличных"}, {"amount": 100}], ["Снятие наличных"]),
    ([{"amount": 100}], []),
])
def test_transaction_descriptions(transactions, expected):
    assert list(transaction_descriptions(transactions)) == expected

def test_card_number_generator():
    """Функция для тестирования генератора, формирующего номера банковских карт в определенном формате"""
    cards = card_number_generator(10, 12)
    assert list(cards) == ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]
