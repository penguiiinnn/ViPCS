def count_even(arr):
    count = 0

    for x in arr:
        if x % 2 == 0:
            count += 1

    return count


def test():
    print(count_even([1, 2, 3, 4, 6]))


def main():
    arr = list(map(int, input("Введите числа через пробел: ").split()))
    print(count_even(arr))


test()
main()