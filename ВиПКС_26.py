def compare_files():
    file1 = r"C:\Users\Настя\Downloads\text1.txt"
    file2 = r"C:\Users\Настя\Downloads\text2.txt"

    with open(file1, "r", encoding="utf-8") as f1:
        text1 = f1.read()

    with open(file2, "r", encoding="utf-8") as f2:
        text2 = f2.read()

    return text1 == text2


def test():
    print(compare_files())


test()