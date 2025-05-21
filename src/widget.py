from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """
    Обрабатывает информацию о карте или счете и возвращает строку с маскировкой номера.
    """
    card_or_account_list = card_or_account.split()
    if "Счет" in card_or_account_list:
        return f"Счет {get_mask_account(card_or_account_list[1])}"
    elif "MasterCard" in card_or_account_list or "Maestro" in card_or_account_list:
        return f"{card_or_account_list[0]} {get_mask_card_number(card_or_account_list[1])}"
    elif "Visa" in card_or_account_list:
        numbers = []
        names = []
        for i in card_or_account_list:
            if i.isdigit():
                numbers.append(i)
            if i.isalpha():
                names.append(i)
        str_numbers = "".join(numbers)
        return f"{names[0]} {names[1]} {get_mask_card_number(str_numbers)}"
    return card_or_account


def get_date(my_date: str) -> str:
    """
    Принимает строку даты в различных форматах ISO и возвращает строку в формате ДД.ММ.ГГГГ.
    """
    date_formats = [
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%dT%H",
        "%Y-%m-%dT",
        "%Y-%m",
        "%Y",
        "%H:%M:%S.%f",
        "%M:%S.%f",
        "%S.%f",
        "%f",
    ]
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(my_date, fmt)
            return date_obj.strftime("%d.%m.%Y")
        except ValueError:
            continue
    raise ValueError("Неверный формат даты")
