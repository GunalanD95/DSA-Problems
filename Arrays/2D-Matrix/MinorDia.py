'''
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.

Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).

'''

# 1) Brute Force

def MinorDiaSum1(A):
    rows = len(A)
    cols = len(A[0])

 
    M = cols  + 1
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if (i+1) + (j+1) == M:
                sum += A[i][j]

    return sum


# Time Complexity: O(N^2)
# Space Complexity: O(1)


# 2 ) - Optimized Solution

def MinorDiaSum(A):
    rows = len(A)
    cols = len(A[0])
    M = len(A)
    sum = 0
    for i in range(rows):
         sum += A[i][M-i-1]                                              # [M-i-1] is the index of the column in the minor diagonal
    return sum


# Time Complexity: O(N)
# Space Complexity: O(1)












if __name__ == '__main__':
    A = [[1, -2, -3],
        [-4, 5, -6],
        [-7, -8, 9]]

    # A = [[3, 2],
    #     [2, 3]]
    print(MinorDiaSum(A))