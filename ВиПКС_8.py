def f(x):  #заданная функция
    return -x**10 + 10*x  #пример

def find_max(a, b, step=0.01):  #поиск максимума
    x = a  #начальная точка
    max_val = f(x)  #начальное значение

    while x <= b:  #пока не дошли до конца
        if f(x) > max_val:  #если нашли больше
            max_val = f(x)  #обновляем максимум
        x += step  #увеличиваем x

    return max_val  #возвращаем максимум

def test():  #тест
    print(find_max(0, 5))  #пример

test()  #запуск