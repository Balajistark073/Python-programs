str1=input("enter string 1: ")
str2=input("enter string 2: ")
sorted1=sorted(str1)
list1=list(str1.upper())
list2=list(str2.upper())
if list1.sort()==list2.sort():
    print('Yes,anagram')
else:
    print('Not a anagram')