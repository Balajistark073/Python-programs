str1=input("enter string: ")
s,e=map(int,input("enter star,end: ").split())
resstr=""
resstr=str1*e
print(resstr)
if resstr[s-1]==resstr[e-1]:
        print("YES")
else:
        print("NO")