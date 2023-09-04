str1=input("enter: ")
'''print(str1.replace(" ",""))'''
joined=""
for char in str1:
    if (char==" "):
        '''joined=joined+""'''
        continue
    else:
        joined=joined+char
print(joined)