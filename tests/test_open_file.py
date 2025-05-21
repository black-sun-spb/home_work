from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.open_file import read_csv_file, read_excel_file


@patch("csv.reader")
def test_read_csv_file(mock_csv_reader: Any) -> Any:
    # Мокаем содержимое файла: первая строка - заголовки, далее - данные
    mock_csv_reader.return_value = iter(
        [
            ["id", "state", "date", "amount", "currency_name", "currency_code", "description", "from", "to"],
            [
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "USD",
                "USD",
                "Test description",
                "from_value",
                "to_value",
            ],
        ]
    )

    m = mock_open(read_data="")  # Мокаем open
    with patch("builtins.open", m):
        result = read_csv_file("transaction.csv")
        expected = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {"amount": 16210.0, "currency": {"name": "USD", "code": "USD"}},
                "description": "Test description",
                "from": "from_value",
                "to": "to_value",
            }
        ]
        assert result == expected
        # Проверяем вызов open с правильными аргументами
        m.assert_called_with("transaction.csv", "r", encoding="utf-8")


def test_read_excel_file() -> Any:
    # Создаем тестовые данные
    data = {
        "id": [1],
        "state": ["done"],
        "date": ["2023-10-01"],
        "amount": [100.0],
        "currency_name": ["USD"],
        "currency_code": ["USD"],
        "description": ["Test transaction"],
        "from": ["Account1"],
        "to": ["Account2"],
    }
    df = pd.DataFrame(data)
    # Сохраняем в Excel файл
    filename = "test.xlsx"
    df.to_excel(filename, index=False)

    # Вызываем функцию
    result = read_excel_file(filename)

    # Проверяем результат
    expected = [
        {
            "id": 1,
            "state": "done",
            "date": "2023-10-01",
            "operationAmount": {"amount": 100.0, "currency": {"name": "USD", "code": "USD"}},
            "description": "Test transaction",
            "from": "Account1",
            "to": "Account2",
        }
    ]

    assert result == expected
