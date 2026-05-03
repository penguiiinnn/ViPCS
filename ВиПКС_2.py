import random

rows, cols = 100, 200
arr = [[random.randint(-3, 10) for _ in range(cols)] for _ in range(rows)]

# вывод массива
for row in arr:
    for x in row:
        print(f"{x:3}", end=" ")
    print()
print("Массив заполнен")