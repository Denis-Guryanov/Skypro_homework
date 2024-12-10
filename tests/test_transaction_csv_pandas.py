from unittest.mock import patch

import pandas as pd

from src.transaction_csv_pandas import read_csv, read_excel


@patch("pandas.read_csv")
def test_read_csv(mock_csv_reader):
    """Функция тестирующая чтение данных из CSV файла"""
    mock_csv_reader.return_value = pd.DataFrame({"ID": [90], "state": ["EXECUTED"]})
    assert read_csv("id,state\\n50,EXECUTED") == [{"ID": 90, "state": "EXECUTED"}]


@patch("pandas.read_excel")
def test_read_excel(mock_excel_reader):
    """Функция тестирующая чтение данных из EXCEL файла"""
    mock_excel_reader.return_value = pd.DataFrame({"ID": [90], "state": ["EXECUTED"]})
    assert read_excel("id,state\\n50,EXECUTED") == [{"ID": 90, "state": "EXECUTED"}]
