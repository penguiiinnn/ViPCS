class Student:
    def __init__(self):
        self.fio = input("ФИО: ")
        self.birth = input("Дата рождения: ")
        self.university = input("Вуз: ")
        self.faculty = input("Факультет: ")
        self.group = input("Группа: ")


def main():
    person = Student()

    print(person.fio)
    print(person.birth)
    print(person.university)


main()