'''
You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.

Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

'''

def MainDaiSum(A):
    rows = len(A)
    cols = len(A[0])
  

    sum  = 0

    for i in range(rows):
        x = i                                                          # x is the row index of the main diagonal element
        y = 0                                                          # y is the column index of the main diagonal element

        while y < cols:                                                
            if x == y:                                                 # if x and y are equal, then the element is the main diagonal element
                sum += A[x][y]                                         # add the element to the sum
            y += 1

    return sum
        









if __name__ == '__main__':
    A = [[1, -2, 3],[-4, 5, -6],[-7, 8, 9]]
    A = [[3, 2],
        [2, 3]]
    print(MainDaiSum(A))