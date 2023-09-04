n=int(input("year: "))
if n%4==0 :
    if n%400==0 :
        print(" leap")
    elif n%100==0 :
        print("not leap")
    else:
        print("leap")
else:
    print("not leap")
