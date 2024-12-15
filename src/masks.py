import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("C:\\Users\\gurya\\PycharmProjects\\Skypro_homework\\logs\\masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее в зашифрованном виде"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Неверный номер карты")
    masked_number_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.info("Данные вывода маски карты получены")
    return masked_number_card


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Неверный номер счета")
    masked_number_account = f"**{account_number[16:]}"
    logger.info("Данные вывода маски счета получены")
    return masked_number_account
