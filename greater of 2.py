num=int(input("enter number"))
unit=num%10
tenth=(num/10)%10
if unit>tenth:
    print(int(unit))
else:
    print((tenth))
 
