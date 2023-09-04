str1 = input("Enter a string: ")
similar_chars = [] 
for i in range(int(len(str1) / 2)):
    if str1[i] == str1[-i - 1]:
        similar_chars.append(str1[i])
if similar_chars:
    print("Similar Alphabets:", ' '.join(similar_chars))
else:
    print("No similar Alphabets")
