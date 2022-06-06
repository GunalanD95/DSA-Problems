'''
You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0.
Specifically, make entire ith row and jth column zero.

'''
# 1) - BruteForce Approach

def Row2ZeroB(A):
    rows = len(A)
    cols = len(A[0])
    C = A
    res = []
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == 0:
                res.append(j)
                A[i] = [0] * cols
                print("o",i,"col",j)

    print("res",res)
    
    for i in range(rows):
        for j in range(cols):
            if j in res:
                C[i][j] = 0

    return C



# 2) - Optimized Approach

def Row2Zero(A):
    rows = len(A)
    cols = len(A[0])

    ColIndx = set()
    RowIndx = set()
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == 0:
                ColIndx.add(j)
                RowIndx.add(i)

    for i in range(rows):
        for j in range(cols):
            if i in RowIndx or j in ColIndx:
                A[i][j] = 0

    return A








if __name__ == '__main__':
    A = [[1,2,3,4],
        [5,6,7,0],
        [9,2,0,4]]

    A = [
        [97, 18, 55, 1, 50, 17, 16, 0, 22, 14],
        [58, 14, 75, 54, 11, 23, 54, 95, 33, 23],
        [73, 11, 2, 80, 6, 43, 67, 82, 73, 4],
        [61, 22, 23, 68, 23, 73, 85, 91, 25, 7],
        [6,  83, 22, 81, 89, 85, 56, 43, 32, 89],
        [0,  6, 1, 69, 86, 7, 64, 5, 90, 37],
        [10, 3, 11, 33, 71, 86, 6, 56, 78, 31],
        [16, 36, 66, 90, 17, 55, 27, 26, 99, 59],
        [67, 18, 65, 68, 87, 3, 28, 52, 9, 70],
        [41, 19, 73, 5, 52, 96, 91, 10, 52, 21]
        ]
    print(Row2Zero(A))