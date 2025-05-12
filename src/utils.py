import json
from typing import Any, Dict, List


def get_transactions_dictionary(file_path: str) -> List[Dict[str, Any]]:
    """A function that loads transactions from a JSON file and returns them as a dictionary."""
    # Path to the file with transactions
    try:
        # Opening the file and loading JSON data
        with open(file_path, "r", encoding="utf-8") as operations:
            transactions = list(json.load(operations))
            if not isinstance(transactions, list):
                raise ValueError(f"Expected a list, but got {type(transactions).__name__}")

            return transactions  # Return the list of transactions

    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        # In case of error, return an empty list
        return []
