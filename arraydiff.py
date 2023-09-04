def arraydiff(list1,list2):
    set1=set(list1)
    set2=set(list2)
    print("The element which is in first array and not in second array is/are",(set1.difference(set2)))
list1,list2=[],[]
no1=int(input("Enter no of elements in 1 st array: "))
for i in range(1,no1+1):
    val=int(input(f"Enter {i} number: "))
    list1.append(val)
no2=int(input("Enter no of elements in 2 nd array: "))
for i in range(1,no2+1):
    val=int(input(f"Enter {i} number: "))
    list2.append(val)
arraydiff(list1,list2)
