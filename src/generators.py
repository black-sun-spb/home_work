from typing import Any, Generator, Iterable, Iterator, Optional


def filter_by_currency(list_of_actions: Iterable[dict[str, Any]], code: Optional[str] = None) -> Iterator:
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    if not list_of_actions:
        return iter([])  # Пустой итератор для пустого списка
    if not code:
        return iter([])  # Пустой итератор для отсутствующего кода
    filtered_transactions = [
        transaction for transaction in list_of_actions if transaction["operationAmount"]["currency"]["code"] == code
    ]
    if not filtered_transactions:
        raise ValueError("Транзакции с таким кодом валюты отсутствуют в списке.")
    return (transaction for transaction in filtered_transactions)


def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if not transactions:
        raise ValueError("Передано пустое значение!")

    for item in transactions:
        if "description" not in item:
            yield "Отсутствует описание"
        else:
            yield item["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, который возвращает номера банковских карт
    в формате XXXX XXXX XXXX XXXX
    """

    for number in range(start, end + 1):
        # Форматируем номер карты: 16 цифр, разделённых пробелами
        card_number = f"{number:016d}"
        formatted_card_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number
