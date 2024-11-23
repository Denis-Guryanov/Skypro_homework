import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "input_data, expected_output, state",
    [
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "EXECUTED",
        ),
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 3, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
            ],
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            "EXECUTED",
        ),
        (
            [
                {"id": 3, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 4, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [],
            "EXECUTED",
        ),
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 2, "state": "FAILED", "date": "2019-07-03T18:35:29.512364"},
            ],
            [{"id": 2, "state": "FAILED", "date": "2019-07-03T18:35:29.512364"}],
            "FAILED",
        ),
    ],
)
def test_filter_by_state(input_data: list[dict], expected_output: list[dict], state: str) -> None:
    assert filter_by_state(input_data, state) == expected_output


def test_sort_by_date() -> None:
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
    ]

    expected_sorted_data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    sorted_data = sort_by_date(data)

    assert sorted_data == expected_sorted_data


def test_sort_by_date_reverse() -> None:
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    expected_sorted_data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    sorted_data = sort_by_date(data, reverse=True)

    assert sorted_data == expected_sorted_data


def test_sort_by_date_no_executed() -> None:
    data = [
        {"id": 3, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
    ]

    sorted_data = sort_by_date(data)

    assert sorted_data == []
