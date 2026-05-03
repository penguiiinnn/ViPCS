import math  #подключаем модуль для sqrt

def vector_length(v):  #функция длины вектора
    return math.sqrt(sum(x*x for x in v))  #корень из суммы квадратов

def test():  #тестовая функция
    v = [3, 4]  #пример вектора
    print(vector_length(v))  

test()  #вызов теста