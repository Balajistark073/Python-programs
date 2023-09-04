'''n=int(input("NO.of Occurance"))
a, b = 0, 1
for i in range(0, n):
    print(a)
    a,b = b, a + b'''
n = int(input("Number of Occurrences: "))
a, b = 0, 1
for i in range(n):
    print(a)
    res = a + b
    a = b
    b = res




