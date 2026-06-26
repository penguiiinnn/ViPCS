def compare_dates(date1, date2):
    d1, m1, y1 = map(int, date1.split("/"))
    d2, m2, y2 = map(int, date2.split("/"))

    if (y1, m1, d1) > (y2, m2, d2):
        return "Первая дата больше"

    if (y1, m1, d1) < (y2, m2, d2):
        return "Вторая дата больше"

    return "Даты равны"


def test():
    print(compare_dates("25/03/2008", "01/09/2007"))


test()