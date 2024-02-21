list1=[88,99,7,6,4]
n=int(input())
for i in range(n):
    list1.append(list1.pop(0))
print(list1)

list1=[88,99,7,6,4]
n=int(input())
n = n % len(list1)
rotated_list = list1[-n:] + list1[:-n]
print(rotated_list)