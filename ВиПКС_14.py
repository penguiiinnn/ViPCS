def trim_spaces(text):
    return text.strip()


def test():
    print(trim_spaces("   уляна кака   "))


def main():
    text = input("Введите строку: ")
    print(trim_spaces(text))


test()
main()