from typing import Dict, List

def filter_by_state(list_of_dictionaries: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """"Функция фильтрации списка словарей"""
    return [item for item in list_of_dictionaries if item.get('state') == state]


def sort_by_date(list_of_dictionaries: List[Dict]) -> List[Dict]:
    """Функция сортировки по дате"""
    return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=True)