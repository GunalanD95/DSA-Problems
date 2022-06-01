'''
Given an integer array A containing N distinct integers, you have to find all the leaders in array A.

An element is a leader if it is strictly greater than all the elements to its right side.

NOTE:The rightmost element is always a leader.

'''

def FindLeaders(A):
    leaders = []
    leaders.append(A[-1])

    maxE = A[-1]

    s = len(A) - 1 
    while s >= 0 :
        if A[s] > maxE:
            maxE = A[s]
            leaders.append(A[s])
        s -= 1

    return leaders


if __name__ == '__main__':
    A = [2, 4, 8, 6]
    print(FindLeaders(A))

