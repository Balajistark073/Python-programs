from collections import Counter
string1=input("enter string:")
result=Counter(string1)
if result.most_common()[0][1]==result.most_common()[1][1]:
    print(0)
else:
    print(result.most_common()[0][0])
print(result.items())
