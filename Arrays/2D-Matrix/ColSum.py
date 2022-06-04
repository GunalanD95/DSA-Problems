'''
Problem Description

You are given a 2D integer matrix A, return a 1D integer vector containing column-wise sums of original matrix.

Input 1:

[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

Output 1:

{15,10,13,16}

'''

def ColSum(A):
    N = len(A)

    numrows = len(A)    # 3 rows in your example
    numcols = len(A[0]) # 4 columns in your example
    res = []

    for i in range(numcols):
        x = 0
        y = i
        
        sum = 0
        while x < N and y <= N:
            sum += A[x][y]
            x += 1
        res.append(sum)
    return(res)


if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(ColSum(A))