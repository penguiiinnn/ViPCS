def digit_sum(n):  #сумма цифр числа
    return sum(map(int, str(abs(n))))  #перевод в строку и суммирование

def find_numbers(N):  #поиск чисел
    for i in range(100, 1000):  #только трёхзначные
        if digit_sum(i) == N:  #если сумма равна N
            print(i, end=" ")  #вывод

def test():  #тест
    find_numbers(5)  #пример

test()  #запуск