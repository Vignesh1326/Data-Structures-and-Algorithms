#Insertion Sort Algorithm
#Best Case O(n)--Array already sorted
#Average Case O(n^2)--All the other cases
#Worst Case O(n^2)--Array sorted in descending

print("Enter the size of array")
n=int(input())
print("Enter the array elements")
a=list(map(int,input().split()))[:n]
for i in range(1,len(a)):
    k=a[i]
    j=i-1
    while(j>=0 and a[j]>k):
            a[j+1]=a[j]
            j=j-1
    a[j+1]=k
print("The sorted array is")
print(a)
