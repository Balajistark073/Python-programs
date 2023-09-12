'''str1="is1 Thi0s T3est 2a"
list1=str1.split()
newlist=[]
for word in list1:
    sortword=sorted(word)
    newlist.append(sortword)
newlist.sort()
for i in newlist:
    print("".join(i),end=" ")'''

str1="is1 Thi0s T3est 2a"
list1=str1.split()
digit="0123456789"
resstr=""
digitlist=[]
for word in list1:
    for j in word:
        if j in digit:
            digitlist.append(j)
digitlist.sort()
for i in digitlist:
    for word in list1:
        if i in word:
            resstr+=word+" "
print(resstr)

'''str1 = "is1 Thi0s T3est 2a"
list1 = str1.split()  # Split the string into a list of words

# Sort the list of words based on their digits
sorted_list = sorted(list1, key=lambda word: ''.join(filter(str.isdigit, word)))

# Join the sorted words into a single string
output_str = ' '.join(sorted_list)

print(output_str)'''



