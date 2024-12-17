from collections import Counter

from src.with_re import count_operations, search_description

test_data = [
    {"description": "Payment to John"},
    {"description": "Payment to Lucy"},
    {"description": "Withdraw from ATM"},
    {"description": "Deposit to savings"},
    {"description": "Payment to John"},
]


def test_search_description():
    assert search_description(test_data, "Payment") == [
        {"description": "Payment to John"},
        {"description": "Payment to Lucy"},
        {"description": "Payment to John"},
    ]

    assert search_description(test_data, "ATM") == [{"description": "Withdraw from ATM"}]

    assert search_description(test_data, "NotFound") == []


def test_count_operations():
    counted = count_operations(test_data)
    expected_count = Counter(
        {"Payment to John": 2, "Payment to Lucy": 1, "Withdraw from ATM": 1, "Deposit to savings": 1}
    )

    assert counted == expected_count
