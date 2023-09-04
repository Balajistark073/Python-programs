def generate_term(n):
    if n == 1:
        return "3"
    elif n == 2:
        return "4"
    else:
        if n % 2 == 1:
            return generate_term(n // 2) + "3"
        else:
            return generate_term(n // 2) + "4"

n = int(input("Enter the value of n: "))
result = generate_term(n)
print(result)
 