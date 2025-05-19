import csv

import pandas as pd


def read_csv_file(file_path: str) -> list[dict]:
    """Функция считывает CSV файл и возвращает список словарей"""
    result_read = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        for row in reader:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": float(row[header.index("amount")]),
                    "currency": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    },
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")],
            }
            result_read.append(row_dict)
    return result_read


if __name__ == "__main__":
    result = read_csv_file("../data/transactions.csv")
    print(result)


def read_excel_file(file: str) -> list[dict]:
    """Функция считывает файл excel и возвращает список словарей"""
    df = pd.read_excel(file)
    result_read = []
    row_count = len(df)
    for n in range(0, row_count):
        row_dict = {
            "id": df.at[n, "id"],
            "state": df.at[n, "state"],
            "date": df.at[n, "date"],
            "operationAmount": {
                "amount": df.at[n, "amount"],
                "currency": {
                    "name": df.at[n, "currency_name"],
                    "code": df.at[n, "currency_code"],
                },
            },
            "description": df.at[n, "description"],
            "from": df.at[n, "from"],
            "to": df.at[n, "to"],
        }
        result_read.append(row_dict)
    return result_read


if __name__ == "__main__":
    result = read_excel_file("../data/transactions_excel.xlsx")
    print(result)
