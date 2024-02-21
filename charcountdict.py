'''arr=[1,1,1,3,3,5,10,10,22]
charcount={}
for char in arr:
    if char in charcount:
        charcount[char]+=1
    else:
        charcount[char]=1
for char,count in charcount.items():
    if count>=2:
        print(char,"->",count)'''
arr = [1, 1, 1, 3, 3, 5, 10, 10, 22]
prev = arr[0]
count = 1
for i in range(1, len(arr)):
    if arr[i] == prev:
        count += 1
    else:
        if count >= 2:
            print(prev, "->", count)
        prev = arr[i]
        count = 1
if count >= 2:
    print(prev, "->", count)
