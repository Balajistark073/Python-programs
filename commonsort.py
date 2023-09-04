nlist1=int(input("Enter no of elements in list1: "))
list1=[int(input(f"Enter element {i+1} ")) for i in range(nlist1)]
nlist2=int(input("Enter no of elements in list2: "))
list2=[int(input(f"Enter element {i+1} ")) for i in range(nlist2)]
common=[]
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
n=len(common)
for i in range(n):
    for j in range(0,n-i-1):
        if common[j]>common[j+1]:
            common[j],common[j+1]=common[j+1],common[j]

#result=sorted(set(common))
for i in common:
    print(i,end=" ") 