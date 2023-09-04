m=int(input("enter num: "))
n=int(input("enter end num: "))
div=0
nondiv=0
for i in range (1, n+1):
    if i%m==0:
        div+=i
    else:
        nondiv+=i
print(nondiv-div)

