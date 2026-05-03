def is_prime(n):  #проверка на простое число
    if n < 2:  #числа меньше 2 не простые
        return False
    for i in range(2, int(n**0.5) + 1):  #проверка до корня
        if n % i == 0:  #если делится
            return False
    return True  #иначе простое

def find_primes(N):  #поиск простых до N
    for i in range(2, N + 1):  #перебор чисел
        if is_prime(i):  #если простое
            print(i, end=" ")  #вывод

def test():  #тест
    find_primes(25)  #пример

test()  #запуск