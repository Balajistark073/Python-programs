arr=[66,18,1,2,377,546]
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)