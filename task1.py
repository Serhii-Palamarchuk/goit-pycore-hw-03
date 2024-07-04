# Завдання 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime

def get_days_from_today(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.now()
    return (today - date).days

print(get_days_from_today('2023-10-09'))