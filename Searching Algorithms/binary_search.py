#BINARY SEARCH
#sorted input, random access, eliminates half of list, O(n log(n))
#narrow the search, works well for large sets of data, faster than linear search
import time
def binarySearch(arr, s, e, x):
    while s <= e: 
        mid = s + (e - s) // 2; 
        if arr[mid] == x: 
            return mid
        elif arr[mid] < x: 
            s = mid + 1 
        else: 
            e = mid - 1
    return -1
arr = [25,0,100,56,7,9,3,11]
arr.sort()
print("Enter the element to be searched")
x=int(input())
st=time.time()
result = binarySearch(arr, 0, len(arr)-1, x)
et=time.time()
if result != -1: 
    print ("Element is present in the array") 
else: 
    print ("Element is not present in array") 
print("Time of execution",et-st)
