#Binary Search

def BinarySearch(arr, low, high, x):

    if high >= low:
 
        mid = (low + high) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return BinarySearch(arr, low, mid - 1, x)
 
        else:
            return BinarySearch(arr, mid + 1, high, x)
 
    else:
        return -1

#Initialize
array = [1,2,3,4,5,6,7,8,9]
toFind = 6

#Search Call
res = BinarySearch(array, 0, len(array)-1, int(input("Enter element to search : ")))

if res != -1:
    print("Element is present at index - ", res)
else:
    print("Element is not present in array.")