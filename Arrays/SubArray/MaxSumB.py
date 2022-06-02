'''
You are given an integer array C of size A. 
Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B. - This is Important here 
'''

import sys

# 1) BruteForce Approach  using carry forward

def maxSubArrayB(A, n,B):
    max_sum = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += A[j]
            if sum <= B:
                max_sum = max(max_sum, sum)
    return max_sum


# Time Complexity: O(N^2)
# Space Complexity: O(1)


############################################################################################################################

# Not Possible to Optimize





if __name__ == '__main__':
    A = [2, 1, 3, 4, 5]
    B = 12  
    N = len(A)

    N = 3
    B = 1
    A = [2, 2, 2]


    N = 5
    B = 7
    A = [ 3, 8, 8, 9, 7 ]

    # N = 9
    # B = 78
    # A = [ 7, 1, 8, 5, 8, 5, 3, 3, 5 ]

    print(maxSubArrayB(A,N,B))

