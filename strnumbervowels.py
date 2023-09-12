str1 = input("Enter string: ")
rev = str1[::-1]
listrev = list(rev)
result = ""
pos = []
vowels = "aeiouAEIOU"
for index, char in enumerate(str1):
    if char in vowels:
        pos.append(index)
filtered_listrev = []
for i, char in enumerate(listrev):
    if i not in pos:
        filtered_listrev.append(char)
result = ''.join(filtered_listrev)
print(result)
