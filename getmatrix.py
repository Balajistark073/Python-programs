m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
strong_point_count = 0
matrix = []
for i in range(m):
    row = list(map(int, input(f"Enter elements for row {i + 1} (space-separated): ").split()))
    matrix.append(row)
for i in range(m):
    for j in range(n):
        current_element = matrix[i][j]
        is_strong_point = True
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if 0 <= i + di < m and 0 <= j + dj < n and matrix[i + di][j + dj] > current_element:
                    is_strong_point = False
                    break
            if not is_strong_point:
                break
        if is_strong_point:
            strong_point_count += 1
print(f"Number of strong points in the matrix: {strong_point_count}")
