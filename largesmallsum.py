def largesmallsum(arr):
    arrodd = []
    arreven = []
    for i in range(len(arr)):
        if i % 2 == 0:
            arreven.append(arr[i])
        else:
            arrodd.append(arr[i])
    arrodd.sort()
    print(arrodd)
    arreven.sort()
    print(arreven)
    print(arrodd[1]+arreven[-2])
arr = []
arr= list(map(int,input("Enter array elements: ").split()))
largesmallsum(arr)
