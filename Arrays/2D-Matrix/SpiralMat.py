'''
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.
'''



def GenSpiral(A):
    N = A**2
    print("N:",N)

    rows, cols = A, A
    C = [[0 for i in range(cols)] for j in range(rows)]


    top = 0
    down = len(C) - 1

    left = 0
    right = len(C[0])  -1 


    # dir = 'r'
    val = 1
    dir = 0


    # Approach using direction string as a variable 
    # 1. start from top left corner and move right
    # 2. move from top right corner and move down
    # 3. move from right to left
    # 4. move from bottom to top
    # 5. repeat

    while left<= right and top <= down:

        # if dir == 'r':
        if dir == 0:
            for i in range(left,right+1):
                C[top][i] = val
                val += 1

            top += 1
            # dir = 'd'
            

        # elif dir == 'd':
        elif dir == 1:
            i = top
            e = down
            while  i <= down:
                C[i][right] = val
                val += 1
                i += 1

            right -= 1
            # dir = 'l'

        # elif dir == 'l':
        elif dir == 2:    
            i = right
            e = left

            while i >= e:
                C[down][i] = val
                val += 1
                i -= 1

            down -= 1
            # dir = 't'
        

        # elif dir == 't':
        elif dir == 3:
            i = down
            e = top

            while i >= e:
                C[i][left] = val
                val += 1
                i -= 1

            left += 1
            # dir = 'r'

        dir=(dir+1) % len(C)

    print("C:",C)


if __name__ == '__main__':
    A = 2
    A = 3
    print(GenSpiral(A))