def is_lucky(n):  #проверка билета
    s = str(n).zfill(6)  #делаем 6 цифр
    return sum(map(int, s[:3])) == sum(map(int, s[3:]))  #сравнение сумм

def count_lucky():  #подсчёт
    count = 0  #счётчик

    for i in range(1000000):  #все билеты
        if is_lucky(i):  #если счастливый
            count += 1  #увеличиваем счётчик

    return count  #возвращаем результат

def test():
    print("Количество счастливых билетов:", count_lucky())

test()