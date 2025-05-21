from src.open_file import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.search import search_transactions_by_description
from src.utils import get_transactions_dictionary
from src.widget import get_date, mask_account_card

valid_states = {"EXECUTED", "CANCELED", "PENDING"}


def main() -> None:
    """Основная функция, связывающая модули и управляющая логикой программы."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = get_transactions_dictionary("data/transactions.json")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = read_csv_file("data/transactions.csv")
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = read_excel_file("data/transactions_excel.xlsx")
    else:
        print("Некорректный выбор. Завершение программы.")
        return

    state = ""
    while state.upper() not in valid_states:
        state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию." 
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
        )
        if state.upper() not in valid_states:
            print(f'Программа: Статус операции "{state}" недоступен.')

    filtered_transactions = filter_by_state(transactions, state.upper())
    print(f'Программа: Операции отфильтрованы по статусу "{state.upper()}"')

    sort_answer = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ")
    if sort_answer.lower() == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию? \nПользователь: ")
        reverse = order.lower() != "по возрастанию"
        filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse)

    rub_only = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ")
    if rub_only.lower() == "да":
        filtered_transactions = [
            t for t in filtered_transactions if t.get("operationAmount", {}).get("currency", {}).get("name") == "руб."
        ]

    search_word = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    )
    if search_word.lower() == "да":
        keyword = input("Введите слово для поиска в описании: ")
        filtered_transactions = search_transactions_by_description(filtered_transactions, keyword)

    if not filtered_transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Программа: Распечатываю итоговый список транзакций...")
    print(f"\nПрограмма: Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    for transaction in filtered_transactions:
        date = get_date(transaction["date"])
        description = transaction["description"]
        from_ = mask_account_card(transaction.get("from", "")) if transaction.get("from") else ""
        to = mask_account_card(transaction.get("to", "")) if transaction.get("to") else ""
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        print(f"{date} {description}")
        if from_ and to:
            print(f"{from_} -> {to}")
        elif to:
            print(f"-> {to}")
        elif from_:
            print(f"{from_} ->")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
