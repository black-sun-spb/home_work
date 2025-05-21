import json
import logging
from json import JSONDecodeError
from typing import Optional

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_dictionary(path: Optional[str] = None) -> list:
    """
    Загружает список транзакций из JSON-файла.

    :param path: Путь к JSON-файлу. Может быть None, но в таком случае загрузка не состоится.
    :return: Список словарей с данными транзакций или пустой список в случае ошибки.
    """
    if path is None:
        logger.error("Путь к файлу не предоставлен.")
        return []

    try:
        logger.info(f"Получаем данные из файла {path}")
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions = json.load(operations)
            except JSONDecodeError:
                logger.error(f"Ошибка чтения JSON-файла {path}")
                return []

        if not isinstance(transactions, list):
            logger.critical("Список транзакций пуст или имеет неверный формат")
            return []

        return transactions
    except FileNotFoundError as ex:
        logger.error(f"Данные не найдены: {ex}")
        return []
