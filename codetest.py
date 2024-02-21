'''list1=['a','a','b','b','c','c']
list2=[1,2,3]
dict1={
    "brand":"benz","model":"a6","prize":100000000
}
re1=list((x,y,z) for x,y,z in zip(list1[::2],list1[1::2],list2))
#print(re1)
print(dict1)'''

'''
a="balaji"
target="ij"
result=[]
count=0
res=[(x,y) for x in a for y in a if x!=y]
for i in res:
    str1=''.join(i)
    result.append(str1)
if target in result:
    count+=1
print(count)
print(result)'''
