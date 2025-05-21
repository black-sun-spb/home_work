from typing import List, Dict
from collections import Counter

def count_operations_by_category(transactions: List[dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает количество операций по заданным категориям с использованием Counter.
    """
    counter: Counter[str] = Counter({category: 0 for category in categories})
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1
    return dict(counter)
