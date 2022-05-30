'''
Problem Statement:
Given an array A, find the size of the smallest subarray such that it contains at 
least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.
'''

# 1) - BruteForce Approach

# def ClosetMinMax(A):
#     N = len(A)

#     # first we need to find min and max from the array
#     maxV = A[0]
#     minV = A[0]

#     for i in range(0,N):
#         if maxV < A[i]:
#             maxV = A[i]
#         elif minV > A[i]:
#             minV = A[i]

#     ans = N
#     for i in range(N):
#         if A[i] == maxV:
#             for j in range(i+1,N):
#                 if A[j] == minV:
#                     length = j-i+1
#                     print("length:",ans)
#                     ans = min(ans,length)
#                     print("length2:",ans)
#                     break
#         elif A[i] == minV:
#             for j in range(i+1,N):
#                 if A[j] == maxV:
#                     length = j-i+1
#                     print("length:",ans)
#                     ans = min(ans,length)
#                     print("length2:",ans)
#                     break


#     print('Min Length of the subrray:',ans)

# Time Complexity: O(N^2)
# Space Complexity: O(1)

#############################################################################################################################

# 2 - Optimized Approach


def ClosetMinMax(A):
    N = len(A)

    # first we need to find min and max from the array
    maxV = A[0]
    minV = A[0]

    for i in range(0,N):
        if maxV < A[i]:
            maxV = A[i]
        elif minV > A[i]:
            minV = A[i]

    ans = N
    maxIndx = - 1
    minIndx = - 1

    e = len(A) - 1

    while e >= 0:
        if A[e] == minV:
            minIndx = e
            if maxIndx != -1:
                length = maxIndx - minIndx + 1
                ans = min(ans,length)
            
        elif A[e] == maxV:
            maxIndx = e
            if minIndx != -1:
                length = minIndx - maxIndx + 1
                ans = min(ans,length)
        e -=1

    if minV == maxV:
        return 1
    else:
        return(ans)



if __name__ == '__main__':
    A = [1,2,3,1,5,6,1,8,9,20,11,12,20,14,1]
    A = [1, 3]
    A = [2]
    ClosetMinMax(A)