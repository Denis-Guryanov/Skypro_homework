import pytest
from unittest.mock import patch
from src.external_api import get_currency

@pytest.mark.parametrize("to_cur, from_cur, amount, mock_response, expected", [
    ("USD", "EUR", 100, {"result": 90}, 90.00),
    ("RUB", "USD", 50, {"result": 4000}, 4000.00),
    ("GBP", "USD", 200, {"result": 300}, 300.00),
])
@patch("requests.get")
def test_get_currency(mock_get, to_cur, from_cur, amount, mock_response, expected):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = get_currency(to_cur, from_cur, amount)
    assert result == expected

@pytest.mark.parametrize("to_cur, from_cur, amount, mock_status_code", [
    ("USD", "EUR", 100, 404),
    ("RUB", "USD", 50, 500),
])
@patch("requests.get")
def test_get_currency_invalid_responses(mock_get, to_cur, from_cur, amount, mock_status_code):
    mock_get.return_value.status_code = mock_status_code

    with pytest.raises(Exception):
        get_currency(to_cur, from_cur, amount)


