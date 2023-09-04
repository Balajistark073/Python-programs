from collections import Counter
def nonrepeat(line):
    freqcount=Counter(line)
    for i in line:
        if freqcount[i]==1:
            print(i,end=' ')
line=input("Enter string: ")
nonrepeat(line)
        
    
'''from collections import Counter
def nonrepeat(line):
    freqcount = Counter(line)
    most_common = freqcount.most_common()
    for char, count in most_common:
        if count == 1:
            print(char, end=' ')

line = input("Enter string: ")
nonrepeat(line)'''