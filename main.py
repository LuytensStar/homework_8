from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    today_day = datetime(2023, 12, 26)
    next_week = today_day + timedelta(days=7)
    birthday_days = {}
    for user in users:
        name = user['name']
        birthday = user['birthday']
        if birthday.month == today_day.month and birthday.day >= today_day.day and birthday.day < today_day.day+7:
            k = datetime(today_day.year, birthday.month, birthday.day) 
            weekday_day = k.strftime('%A')
            if weekday_day == 'Saturday':
                k += timedelta(days=2)
            elif weekday_day == 'Sunday':
                k += timedelta(days=1)
            birthday_days.setdefault(k.strftime('%A'), []).append(name)
        elif birthday.month == next_week.month and birthday.day < next_week.day:
            k = datetime(next_week.year, birthday.month, birthday.day)
            weekday_day = k.strftime('%A')
            if weekday_day == 'Saturday':
                k += timedelta(days=2)
            elif weekday_day == 'Sunday':
                k += timedelta(days=1)
            birthday_days.setdefault(k.strftime('%A'), []).append(name)
    return birthday_days


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 2).date()},
        {"name": "Ktos tam", "birthday": datetime(1976, 12, 3).date()},
        {"name": "Jan Koum_safas", "birthday": datetime(1976, 12, 6).date()},
        {"name": "Ktos tam_1", "birthday": datetime(1976, 12, 9).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
