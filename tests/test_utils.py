from typing import Any
from unittest.mock import patch

import pytest

from src.utils import get_transactions_dictionary


@pytest.fixture
def get_path() -> str:
    return "../data/operations.json"


@pytest.fixture
def get_wrong_path() -> str:
    return "nothing"


@pytest.fixture
def get_bad_file() -> str:
    return "../data/wrong_operations.json"


@patch("builtins.open")  # подменяем функцию открытия файла
def test_get_transactions_dictionary(open_mock: Any) -> None:
    open_mock.return_value.__enter__.return_value.read.return_value = (
        '[{"name": "dict_for_test"}, {"name": ' '"one_more"}]'
    )
    assert get_transactions_dictionary("any_path_no_matter") == [{"name": "dict_for_test"}, {"name": "one_more"}]
    open_mock.assert_called_once_with("any_path_no_matter", "r", encoding="utf-8")


def test_get_transactions_dictionary_1(get_wrong_path: Any) -> None:
    assert get_transactions_dictionary(get_wrong_path) == []


def test_get_transactions_dictionary_2(get_bad_file: Any) -> None:
    assert get_transactions_dictionary(get_bad_file) == []
