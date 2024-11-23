import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def account_card_test_cases() -> list:
    return [
        {"input": "Виза 1234567812345678", "expected": "Виза 1234 56** **** 5678"},
        {"input": "Счет 12345678901234567890", "expected": "Счет **7890"},
        {"input": "Виза 1234", "expected": "Неверный номер карты или счета"},
        {"input": "Счет 1234567890123456789", "expected": "Неверный номер карты или счета"},
        {"input": "Виза", "expected": "Некорректный ввод"},
    ]


@pytest.mark.parametrize(
    "test_case",
    [
        {"input": "2023-10-15T14:30:00.000", "expected": "15.10.2023"},
        {"input": "2020-02-29T14:30:00.000", "expected": "29.02.2020"},
        {"input": "0001-01-01T00:00:00.000", "expected": "01.01.0001"},
        {"input": "9999-12-31T23:59:59.999", "expected": "31.12.9999"},
    ],
)
def test_get_date_valid(test_case: list[dict]) -> None:
    assert get_date(test_case["input"]) == test_case["expected"]


def test_mask_account_card(account_card_test_cases) -> None:
    for test_case in account_card_test_cases:
        assert mask_account_card(test_case["input"]) == test_case["expected"]


def test_get_date_invalid_format() -> None:
    with pytest.raises(ValueError):
        get_date("15.10.2023T14:30:00.000")
