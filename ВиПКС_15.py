def sort_array(arr):
    arr.sort()
    return arr


def test():
    print(sort_array([3.5, 1.2, 4.8, 2.0]))


def main():
    arr = list(map(float, input("Введите числа: ").split()))
    print(sort_array(arr))


test()
main()