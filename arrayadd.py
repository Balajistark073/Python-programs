listarray=[]
target=int(input("enter target: "))
n=int(input("NUmber of inputs: "))
for i in range(1,n+1):
    element=int(input("enter element"))
    listarray.append(element)
sortedarr=sorted(listarray,reverse=True)
print(listarray)
print(sortedarr)
for i in range (n):
       for j in range(i+1,n):
            if sortedarr[i]-sortedarr[j]==target:
                print(i,j)