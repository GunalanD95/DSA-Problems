'''
You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Input 1:

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

Output 1:

[[10, 10, 10], [10, 10, 10], [10, 10, 10]]
'''

# Brute Force Approach using nested for loop


def AddMat(A, B):
    N = len(A)
    res = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            res[i][j] = A[i][j] + B[i][j]

    return res


# Brute Force Approach using list comprehension and zip

def AddMat(A, B):
    N = len(A)

    res = []
    for i in range(N):
        sum = [x + y for x, y in zip(A[i], B[i])]
        res.append(sum)
    return(res)




# time complexity: O(n^2)
# space complexity: O(n^2)






if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
    print(AddMat(A,B))