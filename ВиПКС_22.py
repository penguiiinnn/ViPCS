import time


def main():
    input("Нажмите Enter первый раз")

    start = time.time()

    input("Нажмите Enter второй раз")

    end = time.time()

    print("Прошло секунд:", end - start)


main()