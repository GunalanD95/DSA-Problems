'''
You are given an integer array C of size A. 
Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.

'''
import sys

# 1 - Brute Force Approach using carry forward

def MaxSubArray(A):
    N = len(A)
    max_sum = -sys.maxsize - 1
    for i in range(N):
        sum = 0
        for j in range(i,N):
            sum += A[j]
            max_sum = max(max_sum,sum)
    return max_sum


# 2 - Kadane's Algorithm

def MaxSubArr(A):
    N = len(A)
    max_sum = -sys.maxsize - 1

    cur_sum = 0
    for i in range(N):
        cur_sum += A[i]
        if A[i] > cur_sum:
            cur_sum = A[i]
        print("cur_sum",cur_sum)
        max_sum = max(max_sum,cur_sum)
        print("max==",max_sum)




# Time Complexity: O(N^2)
# Space Complexity: O(1)

if __name__ == '__main__':
    A = [1, 2, 3, 4, -10]
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  
    print(MaxSubArr(A))