# Binary Search with Recursion

'''
Algo :

 - Divide the sorted space 

 - Compare again and reject left or side space 

 - BIN(n) = O(1) + O(n/2)  --> Recurrence relation 

'''

# Iterative 
# def binarysearch(arr,target):
#     low = 0 
#     high = len(arr) - 1

#     while low <= high:

#         mid = (low + high) // 2
 
#         if arr[mid] == target:
#             return mid

#         if arr[mid] > target:
#             high = mid - 1
#         else:
#             low =  mid + 1
#     return -1

# Recursive

def binarysearch(arr,target,low,high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid 

    if arr[mid] > target:
        return binarysearch(arr,target,low,mid-1)
    else:
        return binarysearch(arr,target,mid+1,high)






A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
print("result",binarysearch(A,131,0,len(A)-1))
