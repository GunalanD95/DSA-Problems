'''
You are given a matrix A, you have to return another matrix which is the transpose of A.

NOTE: Transpose of a matrix A is defined as - AT[i][j] = A[j][i] ; Where 1 ≤ i ≤ col and 1 ≤ j ≤ row

Input 1:
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

Output 1:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''


from re import X


def Transpose(A):
    # N = len(A)

    # rows = len(A)    
    # cols = len(A[0])

    # print("rows:",rows,"cols:",cols)
    # arr = [[0]*rows]*cols
    # print(arr)
    # res = []
    # for row in range(cols):
    #     x = 0
    #     y = row
    #     test = []
    #     while x < N and y <= cols:
    #         print(A[x][y])
    #         arr[y][x] = A[x][y]
    #         test.append(arr[y][x])
    #         x += 1
        
    #     res.append(test)

    # print(res)

    N = len(A)

    rows = len(A)    

    cols = len(A[0])

    arr = [[0]*rows for i in range(cols) ]

    for row in range(cols):

        x = 0

        y = row

        test = []

        while x < N and y <= cols:
            arr[y][x] = A[x][y]
            x += 1

    return(arr)











if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    A = [[24, 63, 39, 81, 84, 30],
        [21, 64, 95, 6, 88, 73],
        [33, 6, 63, 96, 86, 66],
        [62, 88, 23, 52, 94, 77],
        [81, 58, 74, 18, 16, 25],
        [26, 40, 88, 64, 72, 23],
        [45, 44, 86, 92, 50, 26],
        [64, 34, 83, 26, 29, 68],
        [43, 42, 7, 17, 45, 52],
        [94, 25, 62, 19, 95, 77]]

    A =  [
        [21, 62, 16, 44, 55, 100, 16, 86, 29],
        [62, 72, 85, 35, 14, 1, 89, 15, 73],
        [42, 44, 30, 56, 25, 52, 61, 23, 54],
        [5, 35, 12, 35, 55, 74, 50, 50, 80],
        [2, 65, 65, 82, 26, 36, 66, 60, 1],
        [18, 1, 16, 91, 42, 11, 72, 97, 35],
        [23, 57, 9, 28, 13, 44, 40, 47, 98],
        ]


    print(Transpose(A))