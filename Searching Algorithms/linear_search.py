#LINEAR SEARCH
# unsorted input, sequential access, slowest, O(n)
import time
a=[5,22,456,0,33,1,56,100,0]
flag=0
print("Enter the element to be searched")
e=int(input())
st=time.time()
for i in range(0,len(a)):
    if(a[i]==e):
        print("Element found at index ",i)
        flag=1
et=time.time()
if(flag==0):
    print("Element not in array")
print("Time of execution", et-st)
