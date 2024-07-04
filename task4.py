# Завдання 4
# потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Generates a list of users who need to be congratulated on their birthdays within the next 7 days.
    Adjusts for birthdays falling on weekends to the next Monday.

    Parameters:
    users (list): List of dictionaries with 'name' (str) and 'birthday' (str in 'YYYY.MM.DD' format).

    Returns:
    list: List of dictionaries with 'name' (str) and 'congratulation_date' (str in 'YYYY.MM.DD' format).
    """
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        # Convert birthday string to datetime object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Set the birthday to the current year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If the birthday has already passed this year, set it to next year
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Check if the birthday falls within the next 7 days
        if today <= birthday_this_year <= end_date:
            # Adjust for weekends
            if birthday_this_year.weekday() in (5, 6):  # Saturday or Sunday
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            # Add the user to the result list with the congratulation date
            result.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")
            })

    return result

# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.07.10"},
    {"name": "Jane Smith", "birthday": "1990.07.11"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
