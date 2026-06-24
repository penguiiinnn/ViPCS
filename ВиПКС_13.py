def check_matrix(matrix):
    rows = True
    cols = True

    for row in matrix:
        if 0 not in row:
            rows = False

    for j in range(len(matrix[0])):
        found = False

        for i in range(len(matrix)):
            if matrix[i][j] == 0:
                found = True

        if not found:
            cols = False

    return rows and cols


def test():
    matrix = [
        [0, 4],
        [5, 0]
    ]
    print(check_matrix(matrix))


test()