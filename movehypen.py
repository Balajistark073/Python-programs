str1=input("enter string: ")
count=0
final=""
for i in str1:
    if i=='-':
        count+=1
    else:
        final+=i
print("-"*count,final)