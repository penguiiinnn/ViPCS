def count_lines():
    filename = r"C:\Users\Настя\Downloads\text.txt"

    with open(filename, "r", encoding="utf-8") as file:
        return len(file.readlines())


def test():
    print(count_lines())


test()