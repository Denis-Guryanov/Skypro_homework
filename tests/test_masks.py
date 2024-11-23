import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:

    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"

    assert get_mask_card_number("9876543210123456") == "9876 54** **** 3456"


def test_invalid_card_number_length() -> None:
    with pytest.raises(ValueError, match="Неверный номер карты"):
        get_mask_card_number("1234")

    with pytest.raises(ValueError, match="Неверный номер карты"):
        get_mask_card_number("123456789012345678")


def test_invalid_card_number_characters() -> None:
    with pytest.raises(ValueError, match="Неверный номер карты"):
        get_mask_card_number("1234a67812345678")

    with pytest.raises(ValueError, match="Неверный номер карты"):
        get_mask_card_number("1234 5678 1234 5678")


def test_empty_card_number() -> None:
    with pytest.raises(ValueError, match="Неверный номер карты"):
        get_mask_card_number("")


def test_valid_account_number() -> None:
    assert get_mask_account("12345678901234567890") == "**7890"

    assert get_mask_account("98765432109876543210") == "**3210"


def test_invalid_account_number_length() -> None:
    with pytest.raises(ValueError, match="Неверный номер счета"):
        get_mask_account("123456")

    with pytest.raises(ValueError, match="Неверный номер счета"):
        get_mask_account("123456789012345678901234")


def test_invalid_account_number_characters() -> None:
    with pytest.raises(ValueError, match="Неверный номер счета"):
        get_mask_account("1234A678901234567890")

    with pytest.raises(ValueError, match="Неверный номер счета"):
        get_mask_account("1234 5678 9012 3456 7890")


def test_empty_account_number() -> None:
    with pytest.raises(ValueError, match="Неверный номер счета"):
        get_mask_account("")
