arr=[55,44,88,22,7,11,8,9]
min=float('inf')
max=float('-inf')
for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i
print(max)
print(min)
