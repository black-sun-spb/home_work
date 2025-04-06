def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате 0000 00** **** 0000"""

    str_number = str(card_number)
    str_card_number = str_number[0:4] + " " + str_number[4:6] + "** **** " + str_number[-4:]
    return str_card_number


def get_mask_account(account: int) -> str:
    """Маскирует номер банковского счета в формате **0000"""

    str_account = str(account)
    return "**" + str_account[-4:]
