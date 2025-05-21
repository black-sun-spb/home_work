from typing import Dict, List

import pytest

from src.category import count_operations_by_category  # Предполагаемое местоположение функции


@pytest.fixture
def sample_transactions() -> List[Dict[str, str]]:
    return [
        {"description": "Оплата мобильной связи"},
        {"description": "Покупка в магазине"},
        {"description": "Оплата мобильной связи"},
        {"description": "Перевод между счетами"},
        {"description": "Покупка в магазине"},
        {"description": "Оплата интернета"},
    ]


def test_count_operations_by_category_basic(sample_transactions: List[Dict[str, str]]) -> None:
    categories: List[str] = ["мобильной", "магазине", "интернета"]
    expected: Dict[str, int] = {"мобильной": 2, "магазине": 2, "интернета": 1}
    result = count_operations_by_category(sample_transactions, categories)
    assert result == expected


def test_count_operations_by_category_empty_categories(sample_transactions: List[Dict[str, str]]) -> None:
    categories: List[str] = []
    expected: Dict[str, int] = {}
    result = count_operations_by_category(sample_transactions, categories)
    assert result == expected


def test_count_operations_by_category_no_matches(sample_transactions: List[Dict[str, str]]) -> None:
    categories: List[str] = ["авиабилеты", "такси"]
    expected: Dict[str, int] = {"авиабилеты": 0, "такси": 0}
    result = count_operations_by_category(sample_transactions, categories)
    assert result == expected
