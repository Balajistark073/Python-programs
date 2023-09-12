def is_palindrome(num):
    return str(num) == str(num)[::-1]
n = int(input())
while True:
    n += 1
    if is_palindrome(n):
        print(n)
        break
