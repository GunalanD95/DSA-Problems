'''
You are given a n x n 2D A A representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.
'''


def Rotate90(A):
    rows = len(A)                                                         # Get the number of rows
    cols = len(A[0])                                                      # Get the number of columns
    for i in range(rows):                                                 # Loop through the rows
        for j in range(i+1, cols):                                        # Start from the first column and go to the last column
            A[j][i],A[i][j] = A[i][j],A[j][i]                             # Swap the elements in the matrix since we are rotating the matrix

    def rev(A):
        N = len(A)
        s = 0
        e = N - 1
        while s <= e:
            temp = A[s]
            A[s] = A[e]
            A[e] = temp
            s += 1
            e -=1
        return A

    for j in range(rows):
        rev(A[j])                                                         # Reverse the rows

    return A









if __name__ == '__main__':
    A =  [
        [1, 2],
        [3, 4],
    ]
    # A =  [
    #     [1]
    # ]
    print(Rotate90(A))