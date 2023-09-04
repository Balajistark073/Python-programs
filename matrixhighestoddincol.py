m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = []
for i in range(m):
    row_list=[]
    for j in range(n):
        row_list=list(map(int,input(f"Enter elements at row {i+1} (space-seperated): ").split()))
    matrix.append(row_list)
for i in matrix:
    print(" ".join(map(str,i)))