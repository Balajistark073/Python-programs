str1 = input("Enter the 1st name: ")
str2 = input("Enter the 2nd name: ")
str3 = str1 + str2
flames = ["F", "L", "A", "M", "E", "S"]
strlist = list(str3)
strset = set(strlist)
count = len(strset)

for char in strset:
    if char in flames:
        flames.remove(char)

while len(flames) > 1:
    count = (count - 1) % len(flames)
    flames.pop(count)

result = flames[0]
if result == "F":
    print("Friends")
elif result == "L":
    print("Love")
elif result == "A":
    print("Affection")
elif result == "M":
    print("Marriage")
elif result == "E":
    print("Enemies")
elif result == "S":
    print("Siblings")
