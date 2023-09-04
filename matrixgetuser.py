m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = []
for i in range(m):
    row_list=[]
    for j in range(n):
        element=int(input(f"Enter element at row {i+1} and column {j+1} "))
        row_list.append(element)
    matrix.append(row_list)
for i in matrix:
    print(" ".join(map(str,i)))