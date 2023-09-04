str1=input("enter string: ")
reverse_string=""
for i in range(len(str1)-1,-1,-1):
    reverse_string+=str1[i]
print(reverse_string)                            