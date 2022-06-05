'''
You are given two integer matrices A and B having same size(Both having same number of rows (N) and columns (M)).
You have to subtract matrix A from B and return the resultant matrix. (i.e. return the matrix A - B).
If X and Y are two matrices of the same order (same dimensions). 
Then X - Y is a matrix of the same order as X and Y and its elements are obtained by subtracting the elements of 
Y from the corresponding elements of X. Thus if Z = [z[i][j]] = X - Y, then [z[i][j]] = [x[i][j]] – [y[i][j]].
'''

# 1) Brute Force Approach using nested for loop

def SubMat(A,B):


    N = len(A)
    res = A
    for row in range(N):
        for col in range(len(A[row])):
            res[row][col] = A[row][col] - B[row][col]
    print(res)
            




if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
    print(SubMat(A,B))