m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = []
for i in range(m):
    row_list = list(map(int, input(f"Enter elements at row {i + 1} (space-separated): ").split()))
    matrix.append(row_list)
for i in matrix:
    print(" ".join(map(str, i)))
max_odd_count = 0
row_with_max_odd_count = None
for i, row in enumerate(matrix):
    odd_count = sum(1 for element in row if element % 2 != 0)   
    if odd_count > max_odd_count:
        max_odd_count = odd_count
        row_with_max_odd_count = i

if row_with_max_odd_count is not None:
    print(f"Row with the highest number of odd elements (row {row_with_max_odd_count + 1}): {matrix[row_with_max_odd_count]}")
else:
    print("No row with odd elements found.")