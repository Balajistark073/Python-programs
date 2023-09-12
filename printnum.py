def withoutdigit(n):
    num="3"
    count=0
    for i in range(1,n+1):
        if num  not in str(i):                                             
            count+=1
    return count
number=int(input())
result=withoutdigit(number)
print(result) 
 






        
