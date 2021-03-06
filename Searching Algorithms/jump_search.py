#JUMP SEARCH
# O(n^1/2), Traverse back only once whereas binary search traverses n logn times
# used when binary search is costly
import time
import math
a=[5,22,456,0,33,1,56,100,0]
a.sort()
flag=0
prev=0
l=len(a)
jump=int(math.sqrt(l))
print("Enter the element to be searched")
e=int(input())
st=time.time()
for i in range(0,len(a)+1,jump):
    if(i>=len(a)):
        for j in range(prev,i):
            if(a[j]==e):
                print("element found at index",j)
                flag=1
                break
    elif(a[i]==e):
        print("Element found at index ",i)
        flag=1
        break
    elif(a[i]>e):
        for j in range(prev,i):
            if(a[j]==e):
                print("element found at index",j)
                flag=1
    if(flag == 1):
        break
    else:
        prev=i
et=time.time()
if(flag==0):
    print("Element not in array")
print("Time of execution", et-st)
