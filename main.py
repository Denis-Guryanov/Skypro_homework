import os
from src.transaction_csv_pandas import read_csv, read_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operation_transaction
from src.with_re import search_description

relative_path_json = "C:\\Users\\gurya\\PycharmProjects\\Skypro_homework\\date\\operations.json"
relative_path_excel = "C:\\Users\\gurya\\PycharmProjects\\Skypro_homework\\date\\transaction.xlsx"
relative_path_csv = "C:\\Users\\gurya\\PycharmProjects\\Skypro_homework\\date\\transactions.csv"
json_path = os.path.abspath(relative_path_json)
excel_path = os.path.abspath(relative_path_excel)
csv_path = os.path.abspath(relative_path_csv)


def get_transactions_from_file() -> list[dict]:
    """Функция, запрашивающая файл для чтения и читающая указанный файл."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    file_handlers = {
        "1": (get_operation_transaction, json_path, "JSON -файл"),
        "2": (read_csv, csv_path, "CSV -файл"),
        "3": (read_excel, excel_path, "XLSX -файл")
    }

    operations_file = None
    while operations_file is None:
        print("Выберите необходимый пункт меню: 1, 2 или 3")
        print("1. Получить информацию о транзакциях из JSON -файла.\n"
              "2. Получить информацию о транзакциях из CSV -файла.\n"
              "3. Получить информацию о транзакциях из XLSX -файла.")
        user_choice = input()

        handler = file_handlers.get(user_choice)
        if handler:
            print(f"Для обработки выбран {handler[2]}")
            operations_file = handler[0](handler[1])
        else:
            print("Неверный ввод")

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    input_status = None
    while input_status not in valid_statuses:
        print("Введите статус, по которому необходимо выполнить фильтрацию. "
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        input_status = input().upper()

        if input_status in valid_statuses:
            print(f"Операции отфильтрованы по статусу {input_status}")
        else:
            print(f"Статус операции {input_status} недоступен")

    filter_operations = filter_by_state(operations_file, input_status)

    data_sort = input("Программа: Отсортировать операции по дате? Да/Нет   ").lower()
    if data_sort == "да":
        order_sort = input("Программа: Отсортировать 'по возрастанию' или 'по убыванию'?   ").lower()
        data_sort_flag = order_sort == "по убыванию"
        filter_order_transactions = sort_by_date(filter_operations, data_sort_flag)
    else:
        filter_order_transactions = filter_operations

    currency_sort = input("Выводить только рублевые транзакции? Да / Нет   ").lower()
    if currency_sort == "да":
        filter_currency_transactions = filter_by_currency(filter_order_transactions, "RUB")
    else:
        filter_currency_transactions = filter_order_transactions

    word_filter = input("Отфильтровать список транзакций по определенному слову в описании?\n"
                        "Введите слово для фильтрации или 'Нет', если фильтровать не нужно: ").lower()
    if word_filter != "нет":
        try:
            filter_word_transactions = search_description(filter_currency_transactions, word_filter)

        except AttributeError:
            print("Транзакции не найдены")
            filter_word_transactions = []

    else:
        filter_word_transactions = filter_currency_transactions

    print("Распечатываю итоговый список транзакций...\n"
          f"Всего банковских операций в выборке: {len(filter_word_transactions)} ")
    print(filter_word_transactions)

    return filter_word_transactions
