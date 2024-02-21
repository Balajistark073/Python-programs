arr=[1,2,3,4,4,5,5,6,2,7,6,5,3,6]
dict1={}
for i in arr:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)
for ele,count in dict1.items():
    print(ele)
