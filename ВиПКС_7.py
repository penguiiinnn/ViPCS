def is_palindrome(n):  #проверка палиндрома
    s = str(n)  #перевод в строку
    return s == s[::-1]  #сравнение с перевёрнутой строкой

def find_palindromes(N):  #поиск до N
    for i in range(N + 1):  #перебор
        if is_palindrome(i):  #если палиндром
            print(i, end=" ")  #вывод

def test():  #тест
    find_palindromes(500)  #пример

test()  #запуск