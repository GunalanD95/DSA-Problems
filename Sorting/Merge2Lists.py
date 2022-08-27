A = [1,2,3,4,5,6]
B = [7,8,9,10,11]

def merge(arr1,arr2):
    m , n = len(arr1) , len(arr2)

    ans = [0] * (m+n)
    print("ans",ans)
    i , j , k = 0 , 0 , 0
    
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            ans[k]= arr1[i]
            i += 1
        else:
            ans[k]= arr2[j]
            j += 1
        k += 1   
        
    while i < m:
        ans[k] = arr1[i]
        k += 1
        i += 1
    while j < n:
        ans[k] = arr2[j]
        k += 1
        j += 1
        
    return ans 
    
    

def mergesort(A,l,r):
    l =



if __name__ == '__main__':
    A = [1,2,3,4,5,6]
    B = [7,8,9,10,11]
    print(merge(A,B))    