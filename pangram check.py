def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    if set(s.lower()) >= alphabet:
        print("Its pangram")
    else:
        print('Not a Pangram') 
s=input("enter string : ")
is_pangram(s)