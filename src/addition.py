import re


def filter_transactions(transactions, search_string):
    """принимаtn список словарей с данными о банковских операциях и строку поиска
    и возвращать список словарей, у которых в описании есть данная строка."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # Фильтруем список словарей
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]

    return filtered_transactions


def categorize_transactions(transactions, categories):
    # Создаем словарь для подсчета операций в каждой категории
    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "")
        for category, pattern in categories.items():
            if re.search(pattern, description, re.IGNORECASE):
                category_counts[category] += 1
                break  # Предполагаем, что каждая операция может относиться только к одной категории

    return category_counts
