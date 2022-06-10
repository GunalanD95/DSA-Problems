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
    
    mid = 1
    min_sum = sys.maxsize
    print(A,B,N,min_sum)
    while mid < N-1:

        # mid to left
        s  = mid - 1
        left  = sys.maxsize
        while  s >= 0:
            if A[mid] > A[s]:
                left = min(left,B[s])     
                print("sum2",left)                                
            s -= 1

        print("lsum",left)

        # mid to right
        e = mid + 1
        right = sys.maxsize 
        while e < N:
            if A[mid] < A[e]:
                right = min(right,B[e])
                
            e += 1
        print("rsum",right)

        tot = left + right + B[mid]
        min_sum = min(tot,min_sum)
        print("min_sum",min_sum)
        mid += 1

    





if __name__ == '__main__':
    A = [1, 3, 5]
    B = [1, 2, 3]

    A = [1, 6, 4, 2, 6, 9]
    B = [2, 5, 7, 3, 2, 7]

    print(MinTreeSum(A,B))