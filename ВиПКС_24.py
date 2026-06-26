from datetime import datetime


def current_date():
    months = [
        "январь", "февраль", "март",
        "апрель", "май", "июнь",
        "июль", "август", "сентябрь",
        "октябрь", "ноябрь", "декабрь"
    ]

    now = datetime.now()

    return f"{now.day}/{months[now.month - 1]}/{now.year}"


def test():
    print(current_date())


test()