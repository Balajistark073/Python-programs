'''str1=input("enter string: ")
str1list=str1.split()
revstr=""
for i in str1list[::-1]:
    revstr+=i+" "
print(revstr)'''

str1=input("enter string: ")
str1list=str1.split()
revstr=""
for i in range(len(str1list) -1,-1,-1):
    revstr+=str1list[i]+" "
print(revstr)
