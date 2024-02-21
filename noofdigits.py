'''n=int(input("ENTER:"))
count=0
for i in str(n):
    count+=1
print(count)'''
n = int(input("ENTER:"))
count = 0  
while n > 0:
    n //= 10
    count += 1
print(count)