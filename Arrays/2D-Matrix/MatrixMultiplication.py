'''
You are given two integer matrices A(having M X N size) and B(having N X P). 
You have to multiply matrix A with B and return the resultant matrix. 
(i.e. return the matrix AB).

Input 1:

 A = [[1, 2],            B = [[5, 6],
      [3, 4]]                 [7, 8]] 

Output 1:

 [[19, 22],
  [43, 50]]

'''

# 1) Brute Force Approach


def MatrixMultiplication(A, B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])


    rows, cols = (rowA, colB)
    C = [[0 for i in range(cols)] for j in range(rows)] 


    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                row = A[i][k]
                col = B[k][j] 
                C[i][j] += row * col
                print("row",row,"col",col,"mul",C[i][j])

    print(C)














if __name__ == '__main__':
    A = [[1, 2],[3, 4]]
    B = [[5, 6],[7, 8]]

    # A = [[1,1]]
    # B = [[2],[3]]
    print(MatrixMultiplication(A,B))