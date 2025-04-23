def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате 0000 00** **** 0000"""

    card_number_without_spaces = card_number.replace(" ", "")
    if len(card_number_without_spaces) != 16:
        return "Номер карты введен не корректно"
    else:
        card_number_mask = (
            f"{card_number_without_spaces[:4]} {card_number_without_spaces[4:6]}** "
            f"**** {card_number_without_spaces[-4:]}"
        )
        return card_number_mask


def get_mask_account(account: str) -> str:
    """Маскирует номер банковского счета в формате **0000"""
    account_number_str = str(account)
    masked_account = "**" + account_number_str[-4:]
    return masked_account
