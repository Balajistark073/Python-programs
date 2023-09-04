row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix = []
for i in range(row):
    rowi = list(map(int, input(f"Enter elements for row {i + 1} (space-separated): ").split()))
    matrix.append(rowi)
leading_sum=0
leading_sum2=0
common_element=0
i=0
while i<row and i<col: 
    leading_sum += matrix[i][i]
    i+=1
i=0
while i<row and i<col:
    leading_sum2 +=matrix[i][col-i-1]
    i+=1
if row % 2 == 1 and col % 2 == 1:
    common_element = matrix[row // 2][col // 2]
print(f"The diagonal sum is {leading_sum+leading_sum2-common_element}")