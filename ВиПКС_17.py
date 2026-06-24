def last_index(text, symbol):
    return text.rfind(symbol)


def test():
    print(last_index("программа", "а"))


def main():
    text = input("Введите строку: ")
    symbol = input("Введите символ: ")
    print(last_index(text, symbol))


test()
main()