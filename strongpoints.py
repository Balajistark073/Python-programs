import numpy as np
matrix = np.zeros((3, 3))
matrix[0, 0] = 56
matrix[0, 1] = 92
matrix[0, 2] = 45
matrix[1, 0] = 19
matrix[1, 1] = 41
matrix[1, 2] = 51
matrix[2, 0] = 55
matrix[2, 1] = 31
matrix[2, 2] = 80
counter = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        is_local_max = True
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (0 <= i + di < matrix.shape[0] and
                    0 <= j + dj < matrix.shape[1] and
                    matrix[i, j] < matrix[i + di, j + dj]):
                    is_local_max = False
                    break
            if not is_local_max:
                break
        if is_local_max:
            counter += 1
print(counter)
