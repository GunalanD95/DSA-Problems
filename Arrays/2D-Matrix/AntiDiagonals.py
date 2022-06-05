'''
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.

'''

# 1) Brute Force Approach 

def diagonal(A):
    N = len(A)
    rows = ((2 * N-1) * N ) // N                                     # row count
    cols = len(A[0])                                                 # col count

    # Pythonic Way of creating 2D Array
    # arr = [[0]*cols]*rows
    # print(arr)

    arr = [[0 for i in range(cols)] for j in range(rows)]           # Pythonic Way of creating 2D Array
    for j in range(N):                                              # looping from top-left to bottom-right
        x  = 0  # row                                               # x = 0
        y =  j  # col                                               # y = j
        while x < N and y >= 0:                               
            arr[x+y][y] = A[y][x]                                   # x + y = row, y = col               
            x += 1
            y -= 1

   
    for k in range(1,N):                                            # looping from top-right to bottom-left
        x  = k     # row
        y =  N -1  # col
        while x < N and y >= 0:
            arr[x+y][y-k] = A[y][x]                                 # x + y = row, y - k = col , y -k will 
            x += 1
            y -= 1
    

    return(arr)



if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(diagonal(A))