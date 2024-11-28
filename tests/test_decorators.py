import pytest

from src.decorators import log


def test_log_func() -> None:
    """Функция, тестирующая функцию возведения в степень без вывода в консоль"""

    @log("")
    def result_function(x: int, y: int):
        return x**y

    result: int = result_function(2, 3)
    assert result == 8


def test_2_log_func() -> None:
    """Тест функции, вызывающей исключение"""

    @log("")
    def result_function() -> None:
        raise Exception("Test Exception")

    with pytest.raises(Exception, match="Test Exception"):
        result_function()


def test_3_log_func() -> None:
    """Функция, тестирующая функцию возведения в степень с выводом информации в файл"""

    @log("func_log.txt")
    def result_function(x: int, y: int):
        return x**y

    result = result_function(1, 5)
    assert result == 1


def test_4_log_func(capsys) -> None:
    @log()
    def result_function(x: int, y: int):
        return x**y

    result = result_function(2, 1)
    captured = capsys.readouterr()
    assert result == 2
    assert "result_function OK" in captured.out
