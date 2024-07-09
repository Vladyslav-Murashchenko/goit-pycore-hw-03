from datetime import datetime

def get_days_from_today(date: str) -> int | str:
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return 'Invalid date format. Please use the format: YYYY-MM-DD'

    today = datetime.today()
    return (today - date).days
