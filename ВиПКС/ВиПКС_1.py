import random

rows, cols = 100, 200
arr = [[random.uniform(-1, 1) for _ in range(cols)] for _ in range(rows)]

#вывод массива
for row in arr:
    for x in row:
        print(f"{x:6.2f}", end=" ")  #форматируем до 2 знаков
    print() #новая строка
print("Массив заполнен")  #новая строка