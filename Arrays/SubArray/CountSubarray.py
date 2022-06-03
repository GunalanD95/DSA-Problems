'''
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.

A = [2, 5, 6]
B = 10
 
The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},

A = [1, 11, 2, 3, 15]
B = 10

The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}
'''

# 1 - Brute Force Approach

def CountSubarryB(A,B):
    N = len(A)
    count = 0
    for i in range(N):
        sum = 0
        for j in range(i,N):
            sum += A[j]
            if sum < B:
                count +=1
    return count


# Time Complexity: O(N^2)
# Space Complexity: O(1)

########################################################################################################################



if __name__ == '__main__':
    A = [2, 5, 6]
    B = 10

    # A = [1, 11, 2, 3, 15]
    # B = 10

    CountSubarryB(A,B)