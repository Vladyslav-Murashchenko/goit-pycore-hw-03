from datetime import datetime, timedelta

UPCOMING_BIRTHDAY_THRESHOLD = 7

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        next_birthday = datetime(today.year, birthday.month, birthday.day).date()

        if (next_birthday < today):
            next_birthday = datetime(today.year + 1, birthday.month, birthday.day).date()

        days_until_birthday = (next_birthday - today).days

        if (days_until_birthday > UPCOMING_BIRTHDAY_THRESHOLD):
            continue

        congratulation_date = next_birthday

        if congratulation_date.weekday() >= 5:
            days_to_add = 7 - congratulation_date.weekday()
            congratulation_date += timedelta(days=days_to_add)

        upcoming_birthdays.append({
            'name': user['name'],
            'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
        })

    return upcoming_birthdays

