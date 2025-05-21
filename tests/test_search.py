from src.search import search_transactions_by_description


def test_search_exact_match() -> None:
    transactions = [
        {"description": "Покупка в магазине"},
        {"description": "Оплата услуг связи"},
        {"description": "Магазин продуктов"},
    ]
    result = search_transactions_by_description(transactions, "магазин")
    assert len(result) == 2
    assert all("магазин" in item["description"].lower() for item in result)


def test_search_case_insensitive() -> None:
    transactions = [
        {"description": "ПОКУПКА В МАГАЗИНЕ"},
        {"description": "магазин"},
    ]
    result = search_transactions_by_description(transactions, "магазин")
    assert len(result) == 2


def test_search_no_matches() -> None:
    transactions = [
        {"description": "Зарплата"},
        {"description": "Оплата аренды"},
    ]
    result = search_transactions_by_description(transactions, "магазин")
    assert result == []


def test_search_empty_list() -> None:
    result = search_transactions_by_description([], "магазин")
    assert result == []


def test_search_missing_description() -> None:
    transactions = [
        {"no_description": "value"},
        {"description": "магазин"},
    ]
    result = search_transactions_by_description(transactions, "магазин")
    assert len(result) == 1
    assert result[0]["description"] == "магазин"


def test_search_special_characters() -> None:
    transactions = [
        {"description": "Покупка (магазин)"},
        {"description": "Что-то еще"},
    ]
    result = search_transactions_by_description(transactions, r"\(магазин\)")
    assert len(result) == 1
    assert "(магазин)" in result[0]["description"]
