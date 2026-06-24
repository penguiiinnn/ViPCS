def sort_strings(strings):
    strings.sort()
    return strings


def test():
    print(sort_strings(["Япония", "Швейцария", "Лихтенштейн", "Босния и Герцеговина", "Черногория"]))


def main():
    strings = input("Введите строки через запятую: ").split(",")
    print(sort_strings(strings))


test()
main()