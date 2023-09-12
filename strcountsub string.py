
str1=input("enter : ")
char1=input("enter char1: ")
char2=input("enter char2: ")
concat=char1+char2
count=0
for i in range(len(str1)-1):
    if str1[i:i+2]==concat:
        count+=1
print(count)


