def printing(n):
     if n<=finish:
        print(n)
        return printing(n+1)
     else:
        return n
finish=int(input("enter ending"))
printing(1)
