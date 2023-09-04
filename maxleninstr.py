str1=input("enter string: ")
str1list=str1.split()
maxlist=[]
for words in str1list:
    maxlist.append(len(words)) 
maxlist.sort()
longlen=maxlist[-1]
print(longlen)
for words in str1list:
    if len(words)==longlen:
        print(words)
        
