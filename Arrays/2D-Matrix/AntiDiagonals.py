'''
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.

'''

# 1) Brute Force Approach 

def diagonal(A):
    N = len(A)
    rows = ((2 * N-1) * N ) // N
    cols = N

    # Pythonic Way of creating 2D Array
    # arr = [[0]*cols]*rows
    # print(arr)

    arr = [[0 for i in range(cols)] for j in range(rows)]
    print(arr)

    
    for j in range(N):
        x  = 0 # row
        y =  j  # col
        c = 0
        while x < N and y >= 0:
            c += 1
            print("c: ", c)
            print(A[x][y],"-","x:y",x,y)
            x += 1
            y -= 1
            
    for k in range(1,N):
        x  = k     # row
        y =  N -1  # col
        while x < N and y >= 0:
            print(A[x][y],"-","x:y",x,y)
            x += 1
            y -= 1



if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(diagonal(A))