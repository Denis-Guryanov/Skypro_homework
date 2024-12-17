from unittest.mock import patch

from main import get_transactions_from_file


@patch("builtins.input", side_effect=["1", "EXECUTED", "да", "по возрастанию", "да", "нет"])
@patch("main.get_operation_transaction", return_value=[{"status": "EXECUTED", "currency": "RUB"}])
@patch("main.filter_by_state", return_value=[{"status": "EXECUTED", "currency": "RUB"}])
@patch("main.sort_by_date", return_value=[{"status": "EXECUTED", "currency": "RUB"}])
@patch("main.filter_by_currency", return_value=[{"status": "EXECUTED", "currency": "RUB"}])
@patch("main.search_description", return_value=[{"status": "EXECUTED", "currency": "RUB"}])
def test_get_transactions_from_file(
    mock_search_description,
    mock_filter_by_currency,
    mock_sort_by_date,
    mock_filter_by_state,
    mock_get_operation_transaction,
    mock_input,
):

    result = get_transactions_from_file()

    assert result is not None
    assert len(result) == 1
    assert result[0]["status"] == "EXECUTED"
    mock_get_operation_transaction.assert_called_once()
    mock_filter_by_state.assert_called_once()
    mock_sort_by_date.assert_called_once()
    mock_filter_by_currency.assert_called_once()
