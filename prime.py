n = int(input("enter start range: "))
m = int(input("enter end range: "))
count = 0
for i in range(n, m + 1):
    is_prime = True
    if i <= 1:
        is_prime = False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print(count)
