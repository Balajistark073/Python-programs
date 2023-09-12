def rotate_clockwise(matrix):
    return list(map(list, zip(*matrix[::-1])))
def rotate_counterclockwise(matrix):
    return list(map(list, zip(*matrix)))[::-1]
def alternate_layer_rotation(matrix):
    rows, cols = len(matrix), len(matrix[0])
    min_dimension = min(rows, cols)
    for layer in range(min_dimension // 2):
        if layer % 2 == 0:
            rotated_layer = rotate_clockwise([row[layer:cols - layer] for row in matrix[layer:rows - layer]])
            for i in range(layer, rows - layer):
                matrix[i][layer:cols - layer] = rotated_layer[i - layer]
        else:
            rotated_layer = rotate_counterclockwise([row[layer:cols - layer] for row in matrix[layer:rows - layer]])
            for i in range(layer, rows - layer):
                matrix[i][layer:cols - layer] = rotated_layer[i - layer]
    return matrix
m = int(input())
n = int(input())
matrix = []
for i in range(m):
    row_list = list(map(int, input().split()))
    matrix.append(row_list)
rotated_matrix = alternate_layer_rotation(matrix)
for row in rotated_matrix:
    print(*row)
