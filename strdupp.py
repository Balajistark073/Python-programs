from collections import Counter
str1=input("enter: ")
result=Counter(str1)
lista=result.most_common()
print(lista)
for i in lista:
    if i[1]>1:
        print(i[0])

