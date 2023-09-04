'''from collections import Counter
str1=input("enter: ")
result=Counter(str1)
print(result.most_common())'''
str1=input("enter: ")
counted={}
for char in str1:
    if char in counted:
        counted[char]+=1
    else:
        counted[char]=1
for char,count in counted.items():
    print(char, ":" ,count)
#print(counted.items())