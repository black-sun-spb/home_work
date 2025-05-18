from datetime import datetime
from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Фукнция принимает на вход список словарей и выдает новый список с заданным ключом"""
    new_list = []
    for key in list_dict:
        if key.get("state") == state:
            new_list.append(key)
    return new_list


def sort_by_date(list_of_values: list[dict], reverse: bool = True) -> list[dict]:
    """Возвращает список, отсортированный по дате"""
    return sorted(list_of_values, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=reverse)
