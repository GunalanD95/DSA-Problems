'''
Problem Description

You are given a 2D integer matrix A, return a 1D integer vector containing column-wise sums of original matrix.

Input 1:

[1,2,3,4]
[5,6,7,8]
[9,2,3,4]


Example Output

Output 1:

{10,26,18}

'''

def RowsSum(A):
    N = len(A)

    numrows = len(A)    # 3 rows in your example
    numcols = len(A[0]) # 4 columns in your example
    res = []

    for i in range(numrows):
        sum = 0
        for j in range(numcols):
            sum += A[i][j]
        res.append(sum)
    return res


if __name__ == '__main__':
    A = [[1,2,3,4],
        [5,6,7,8],
        [9,2,3,4]]
    print(RowsSum(A))