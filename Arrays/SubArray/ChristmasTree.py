'''
You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.

You are to choose 3 trees such that their total cost is minimum. Return that cost.

If it is not possible to choose 3 such trees return -1.
'''

# 1) Brute Force
import sys

def MinTreeSum(A,B):
    N = len(A)
    if N < 3:
        return - 1
    
    mid = 1                                           # mid is the index of the middle element of the array
    min_sum = sys.maxsize
    while mid < N-1:

        # find left most min element for mid
        s  = mid - 1                                  # s is the index of the left most min element of the array
        left  = sys.maxsize
        while  s >= 0:                                # loop left to find the left most min element of the array < A[mid]
            if A[mid] > A[s]:
                left = min(left,B[s])                                 
            s -= 1


        # find right most max element for mid
        e = mid + 1                                  # e is the index of the right most max element of the array
        right = sys.maxsize 
        while e < N:                                 
            if A[mid] < A[e]:                        # loop right to find the right most min element of the array > A[mid]
                right = min(right,B[e])
                
            e += 1

        tot = left + right + B[mid]                  # total cost of the 3 indexes
        min_sum = min(tot,min_sum)                   # find the minimum total cost of the 3 trees
        mid += 1

    if min_sum == sys.maxsize:
        return -1
    return min_sum

    





if __name__ == '__main__':
    A = [1, 3, 5]
    B = [1, 2, 3]

    A = [1, 6, 4, 2, 6, 9]
    B = [2, 5, 7, 3, 2, 7]

    print(MinTreeSum(A,B))