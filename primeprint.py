n=int(input("Enter range"))
prime=[]
for i in range(2,n):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
        else:
            continue
    else:
        prime.append(i)
print(prime)