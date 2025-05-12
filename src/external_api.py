import os

from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def convert_from_i_to_rub(transaction: Any) -> Any:
    """Функция запрашивает курс для конвертации заданной валюты"""
    amount = float(transaction["operationAmount"]["amount"])  # получение суммы траты
    currency = transaction["operationAmount"]["currency"]["code"]  # получение валюты
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

        headers = {"apikey": f"{api_key}"}

        response = requests.get(url, headers=headers)
        return round(response.json()["rates"]["RUB"] * amount, 2)
    return amount
