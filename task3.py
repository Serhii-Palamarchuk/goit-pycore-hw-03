# Завдання 3
# Напишіть функцію, яка приймає номер телефону у будь-якому форматі та повертає його у форматі +380501234567.

import re

def normalize_phone(phone_number):
    """
    Normalize a phone number by removing all non-digit characters and adding the international code if necessary.

    Args:
        phone_number (str): The phone number to be normalized.

    Returns:
        str: The normalized phone number.

    """
    # Remove all characters except digits and '+'
    sanitized_number = re.sub(r"[^\d+]", "", phone_number).strip()

    # Check if the number already contains the international code
    if not sanitized_number.startswith('+'):
        # If the number starts with '380', add only '+'
        if sanitized_number.startswith('380'):
            sanitized_number = '+' + sanitized_number
        else:
            # For other cases, add '+38'
            sanitized_number = '+38' + sanitized_number

    return sanitized_number

# Приклад використання
raw_numbers = [
	"067\\t123 4567",
	"(095) 234-5678\\n",
	"+380 44 123 4567",
	"380501234567",
	"    +38(050)123-32-34",
	"     0503451234",
	"(050)8889900",
	"38050-111-22-22",
	"38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)