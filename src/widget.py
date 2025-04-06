from datetime import datetime

from src.masks import get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция маскировки цифр карты и счета"""
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:-1])
    number_card_or_score = string_split[-1]

    return name_card_or_score, number_card_or_score


test = "Visa Platinum 7000792289606361"
name_card, number_card = mask_account_card(test)

masked_number = get_mask_card_number(number_card)
print(f"{name_card}: {masked_number}")


def get_date(my_date: str) -> str:
    """Функция, которая меняет формат даты"""
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
