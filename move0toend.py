arr=[2,0,8,0,5,7,0,3]
for i in arr:
    if i==0:
        arr.remove(i)
        arr.append(0)
print(arr)