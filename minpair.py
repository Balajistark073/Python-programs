arr=[22,33,44,55]
arr1=sorted(arr)
curr=[]
for i in range(len(arr1)-1):
    temp=arr1[i+1]-arr1[i]
    curr.append(temp)
mini=curr.index(min(curr))
for i in range(len(arr1)-1):
    if (arr1[i+1]-arr1[i])==curr[mini]:
        print(arr1[i],arr1[i+1])