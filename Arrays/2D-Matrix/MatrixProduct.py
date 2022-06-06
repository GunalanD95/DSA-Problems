'''
You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.

'''

def MatrixProd(A,B):
    row = len(A)
    col = len(A[0])

    for i in range(row):
        for j in range(col):
            A[i][j] = B * A[i][j]

    return A











if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    B = 2

    print(MatrixProd(A,B))