from Merge2parts import mergearray


# mergesort implementation using recursion 

def MergeSort(arr,l,r):
    print("left",l,"end",r)
    if l == r:
        return 
    # breaking the array into two equal parts
    
    mid = (l+r)//2


    MergeSort(arr,l,mid)
    MergeSort(arr,mid+1,r)
    mergearray(arr,l,mid,r)

    return arr






if __name__ == '__main__':
    A = [5,2,3,1]

    print("Merge-Sort",MergeSort(A,0,len(A)-1))  

'''
tc : o(log n)
'''