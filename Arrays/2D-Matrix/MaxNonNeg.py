'''
Given an array of integers A, of size N.

Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray, return the one having the smallest starting index in A.

NOTE: It is guaranteed that an answer always exists.

'''
import sys

def MaxNonNegs(A):
    N = len(A)

    st_indx = 0
    end_indx = 0 
    length = 0
    res_len = -sys.maxsize - 1
    s1 , e1 = 0 , 0
    bool = False
    for i in range(N):
        if A[i] < 0:
            for j in range(i,N):
                if A[j] > 0:
                    st_indx = j
                    break
        if A[i] >  0:
            end_indx = i
        if end_indx >= st_indx:
            bool = True 
            length = (end_indx -  st_indx)
            if length > res_len:
                res_len = length
                s1 , e1 = st_indx , end_indx
    print("ans1",A[s1:e1+1],"max_len",s1,e1)




# 2 ) Optimized solution

def MaxNonNeg(A):
    N = len(A)
    st_indx , end_indx  = 0 , 0      # temp start and end index of the subarray
    length = 0                       # length of the subarray
    res_len = -sys.maxsize - 1       # max length of the subarray
    s1 , e1 = 0 , 0                  # start and end index of the subarray
    for i in range(N):
        if A[i] < 0:                 # if A[i] is negative then we need to find the next positive element
            st_indx = i+1            # so i + 1
        if A[i] >  0:
            end_indx = i
        if end_indx >= st_indx:
            length = (end_indx -  st_indx)
            if length > res_len:
                res_len = length
                s1 , e1 = st_indx , end_indx

    return(A[s1:e1+1])












if __name__ == '__main__':
    
    A = [1, 2, 3,-1,-2,-1,1,4, 5, 6]
    A = [5, 6, -1, 7, 8,9,7]
    # A = [ -3674875, 5305422, 7665178, 205505, -7168198, -1398091, 5392310, -1700856, 1259052, -3056006 ]
    # A = [ 7251357, -6249230, 3917080, -5577664, -3417609, 2534660, -4723211, -3827311, -3854309, -6641510 ]
    # A = [8986143,-5026827,5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]
    # A = [ -4549634, -3196682, 8455838, -1432628, -263819, -3928366, -5556259, -2114783, 3923939, -4183708 ]
    A = [ -8802046, 445989, -3367042, 6372261, -8338725, 2688067, -3748597, -2880743, -5783594, 1765331 ]


    print(MaxNonNeg(A))