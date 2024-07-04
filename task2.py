# Завдання 2
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей

import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    """
    Generates a sorted list of unique random numbers within a specified range.

    Parameters:
    min (int): The minimum possible number in the set (must be at least 1).
    max (int): The maximum possible number in the set (must be no more than 1000).
    quantity (int): The number of unique numbers to generate (must be between 1 and the range size).

    Returns:
    A sorted list of unique random numbers, or an empty list if parameters are out of range.
    """
    # Check if the input parameters are within the specified constraints
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    # Generate a set of unique random numbers within the specified range
    random_numbers = set()
    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(min, max))

    # Convert the set to a sorted list and return it
    return sorted(random_numbers)

# Example usage
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)