def multiply(A, B):  #функция умножения матриц
    rows = len(A)  #количество строк A
    cols = len(B[0])  #количество столбцов B
    res = [[0]*cols for _ in range(rows)]  #результат

    for i in range(rows):  #по строкам A
        for j in range(cols):  #по столбцам B
            for k in range(len(B)):  #по элементам
                res[i][j] += A[i][k] * B[k][j]  #формула умножения

    return res  #возврат результата

def test():  #тест
    A = [[2, 1], [4, 3]]  #матрица A
    B = [[6, 5], [8, 7]]  #матрица B
    print(multiply(A, B))  #вывод

test()  #запуск