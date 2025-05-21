import re
from typing import Dict, List


def search_transactions_by_description(transactions: List[Dict], query: str) -> List[Dict]:
    """
    Ищет транзакции, содержащие заданную строку в описании.

    Функция принимает список транзакций и строку запроса, использует регулярные выражения для поиска
    совпадений в поле "description" каждой транзакции. Возвращает список транзакций, содержащих
    совпадение в описании.

    :param transactions: Список словарей с транзакциями.
    :param query: Строка для поиска в описании транзакций.
    :return: Список словарей, содержащих транзакции с совпадением.
    """
    pattern = re.compile(query, re.IGNORECASE)
    return [t for t in transactions if "description" in t and pattern.search(t["description"])]
