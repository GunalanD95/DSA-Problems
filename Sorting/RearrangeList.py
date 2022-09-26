'''
Given an array of N elements , we need to rearrange index/value A[0] to its  sorted position .

notes all the values left of A[0] should be <= A[0] and vice versa for the right side of the rearranged array

return the sorted index of A[0] after  rearrangement
'''

def Rearrange(arr,l,r):
    i = l + 1
    j = r

    while i <= j:

        if arr[i] <= arr[l]:
            i += 1

        elif arr[j] > arr[l]:
            j -= 1

        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp 
            i += 1 
            j -= 1


    temp = arr[l]
    arr[l] = arr[i-1]
    arr[i-1] = temp 
    print("arr",arr)
    return i-1

if __name__ == '__main__':
    A = [10,3,8,15,6,12,2,18,7,1]
    A = [2,1]
    print(Rearrange(A,0,len(A)-1))