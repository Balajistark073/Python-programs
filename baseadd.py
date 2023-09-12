def decimal(num,base):
    sum=0
    numstr=str(num)
    for i, digit in enumerate(numstr[::-1]):
            sum+=int(digit)*(base**i)
    return sum
base=int(input())
x,y=map(int,input().split())
number1=decimal(x,base)
number2=decimal(y,base)
print(number1+number2)

'''base=int(input())
x,y=map(int,input().split())
sum=int(str(x),base)+int(str(y),base)
print(sum)    '''