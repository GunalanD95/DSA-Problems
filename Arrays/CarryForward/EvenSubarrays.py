'''
You are given an integer array A.

Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.

Return "YES" if it is possible; otherwise, return "NO" (without quotes).
'''

def EvenSubAr(A):
    N = len(A)

    if N % 2 != 0:
        return "NO"
    else:
        L = N // 2
        F = A[L:][0]
        B = A[:L][-1]

        if F % 2 == 0 and B % 2 == 0:
            return "YES"





if __name__ == '__main__':
    A = [2, 4, 8, 6]
    print(EvenSubAr(A))