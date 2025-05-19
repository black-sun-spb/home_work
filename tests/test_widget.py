from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("value, expected", [("Счет 64886864736788947795", "Счет **7795")])
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "type_and_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card_2(type_and_number: str, expected: str) -> None:
    """Тестируется маскировка номера карты"""
    assert mask_account_card(type_and_number) == expected


@pytest.mark.parametrize(
    "input_date, expected_exception",
    [
        ("неправильная дата", ValueError),
    ],
)
def test_get_date_exceptions(input_date: str, expected_exception: Any) -> None:
    with pytest.raises(expected_exception):
        get_date(input_date)
