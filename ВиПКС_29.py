class Programmer:
    def __init__(self):
        self.fio = input("ФИО: ")
        self.birth = input("Дата рождения: ")
        self.university = input("Вуз: ")
        self.year = input("Год окончания: ")
        self.language = input("Язык программирования: ")
        self.level = input("Уровень владения: ")


def main():
    worker = Programmer()

    print(worker.fio)
    print(worker.language)
    print(worker.level)


main()