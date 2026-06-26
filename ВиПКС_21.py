def F(n):
    if n == 0:
        return 1

    if n == 1:
        return 2

    return 2 * F(n - 1) - F(n - 2)


def test():
    print(F(0))
    print(F(1))
    print(F(5))


def main():
    n = int(input("Введите n: "))
    print(F(n))


test()
main()