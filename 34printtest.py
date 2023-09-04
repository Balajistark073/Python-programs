n = int(input("Enter number: "))
result = ""
convert = bin(n)
strcon = str(convert[2:])
for i in strcon:
    if i == '1':
        result += '3'
    else:
        result += '4'
print(result)


