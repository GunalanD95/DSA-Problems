'''
You are given two matrices A & B of equal dimensions and you have to check whether two matrices are equal or not.

NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j in the given range.

'''

def CheckSame(A,B):
    N = len(A)

    c = 0
    for i in range(N):
        if A[i] == B[i]:
            c += 1
    if c == N:
        print(1)
    else:
        print(0)




















if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    B = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

    # A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    # B = [[1, 2, 3],[7, 8, 9],[4, 5, 6]]

    print(CheckSame(A,B))