

def mergearray(arr,l,y,r):
    ans = [0] * (r-l+1)
    i , j , k = l , y+1 , 0

    while i <= y and j <= r:
        if arr[i] < arr[j]:
            ans[k]= arr[i]
            i += 1
        else:
            ans[k] = arr[j]
            j += 1
        k += 1   
        
    # adding left overs if the loops ends before the end points 
    while i <= y:
        ans[k] = arr[i]
        k += 1
        i += 1
    while j <= r:
        ans[k] = arr[j]
        k += 1
        j += 1
        
    # copy the sorted ones to original array
    counter = 0
    for cp in range(l,r+1):
        arr[cp] = ans[counter]
        counter += 1
        
    return arr
    

if __name__ == '__main__':
    A = [8,1,3,6,11,2,4,9,7,6]
    # merge two parts of array which are sorted 
    print("merge-2",mergearray(A,2,4,7))   