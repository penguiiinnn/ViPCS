def different_digits(n):
    result = []  # список для ответа

    for num in range(n + 1):  # перебираем числа от 0 до n
        s = str(num)  # превращаем число в строку

        if len(s) == len(set(s)):  # если все цифры разные
            result.append(num)  # добавляем число

    return result  # возвращаем результат


def test():
    print(different_digits(30))


def main():
    n = int(input("Введите N: "))
    print(different_digits(n))


test()
main()