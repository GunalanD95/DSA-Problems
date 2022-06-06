'''
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.
'''



def GenSpiral(A):
    N = A**2
    print(N)

    rows, cols = A, A
    C = [[0 for i in range(cols)] for j in range(rows)]

    count = 1
    for i in range(cols):
        for j in range(rows):
            C[i][j] = count
            count += 1

    print(C)

    top = 0
    down = len(C) - 1
    left = 0
    right = len(C[0])  -1 
    dir = 0

    while top <= down and left <= right:
        if dir == 0:
            for i in range(left,right+1):
                print(C[top][i])
            top += 1

        elif dir == 1:
            for i in range(top,down+1):
                print(C[i][right])
            right -= 1

        elif dir == 2:
            # for i in range(right,left):
            for i in range(right,0,-1):
                print(C[down][i])
            down -= 1

        elif dir == 3:
            for i in range(down,top,-1):
                print(C[i][left])
            left += 1

        dir = (dir + 1 ) % 4


        # top += 1
        # left += 1

















if __name__ == '__main__':
    A = 4
    print(GenSpiral(A))