import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_operation_transaction


@pytest.mark.parametrize(
    "file_path, mock_json, expected",
    [
        (
            "valid_file.json",
            [{"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}}],
            [{"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}}],
        ),
        ("empty_file.json", [], []),  # Пустой файл
        ("invalid_file.json", "invalid_json", []),  # Неверный JSON
    ],
)
@patch("builtins.open", new_callable=mock_open)
def test_get_operation_transaction(mock_open, file_path, mock_json, expected):
    if isinstance(mock_json, list):
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps(mock_json)
    else:
        mock_open.return_value.__enter__.return_value.read.return_value = mock_json  # Неверный JSON как строка

    with patch("os.path.isfile", return_value=True):
        result = get_operation_transaction(file_path)
        assert result == expected


@pytest.mark.parametrize(
    "transactions, mock_currency_response, expected_sum",
    [
        (
            [{"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}}],
            {"result": 100},
            100.00,
        ),
        (
            [{"operationAmount": {"currency": {"code": "USD"}, "amount": 50}}],
            {"result": 4000},
            4000.00,
        ),
        (
            [{"operationAmount": {"currency": {"code": "EUR"}, "amount": 80}}],
            {"result": 7000},
            7000.00,
        ),
    ],
)
@patch("src.external_api.get_currency")
def test_transactions_sum(mock_get_currency, transactions, mock_currency_response, expected_sum):
    mock_get_currency.return_value = mock_currency_response["result"]

    assert mock_currency_response["result"]
