def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def column_with_most_primes(matrix):
    if not matrix:
        return None
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_prime_count = 0
    max_prime_column = -1
    for col in range(num_cols):
        prime_count = sum(1 for row in range(num_rows) if isprime(matrix[row][col]))
        if prime_count > max_prime_count:
            max_prime_count = prime_count
            max_prime_column = col
    return max_prime_column
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = []
for i in range(m):
    row_list = list(map(int, input(f"Enter elements at row {i + 1} (space-separated): ").split()))
    matrix.append(row_list)
result=column_with_most_primes(matrix)
for i in matrix:
    print(i[result],end=" ")