
def RevArr(arr,l,mid,r):
    i = l 
    j = mid + 1
    k = 0
    ans = [0] * (r - l + 1)

    while i <= mid and j <= r:

        if arr[i] <= arr[j]:
            ans[k] = arr[i]
            i += 1
        else:
            ans[k] = arr[j]
            j += 1 

        k += 1


        while i <= mid:
            ans[k] = arr[i]
            i += 1
            k += 1

        while j <= r:
            ans[k] = arr[j]
            j += 1 
            k += 1


        counter = 0
        for idx in range(l,r+1):
            arr[idx] = ans[counter]
            counter += 1

        return arr 


def RevSort(arr,l,r):
    if l == r:
        return 

    mid = (l+r) // 2 

    RevSort(arr,l,mid)
    RevSort(arr,mid+1,r)

    return RevArr(arr,l,mid,r)



if __name__ == '__main__':
    A = [2,4,3,5,1]
    print("Merge-Sort",RevSort(A,0,len(A)-1))  