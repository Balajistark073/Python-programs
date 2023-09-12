list1=[1,2,3,4,5,6,7,8,9,0]
n=int(input())
for i in range(n):
    list1.append(list1.pop(0))
print(list1)