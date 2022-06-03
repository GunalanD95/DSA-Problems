'''
Q3. Alternating Subarrays Easy


Problem Description
You are given an integer array A of length N comprising of 0's & 1's, and an integer B.

You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.

A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's. 
For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are no

 A = [1, 0, 1, 0, 1]
 B = 1 
                     0  1  2  3  4
 o/p -  [1, 2, 3] - [1, 0, 1, 0, 1]
 Index 1 acts as a centre of alternating sequence: [A0, A1, A2] - [ 1,0,1 ]
 Index 2 acts as a centre of alternating sequence: [A1, A2, A3] - [ 0,1,0 ]
 Index 3 acts as a centre of alternating sequence: [A2, A3, A4] - [ 1,0,1 ]
'''

# Brute Force Approach 


def AlternateSubArrayB(A,B):
    N = len(A)
    B = 2 * B + 1

    s = 0
    if B == 1:
        e = N -1
    else:
        e = B -1 

    res = []
    while e < N :
        print(s,e)
        print("center",s+1,e-1)
        
        if A[s] == A[e] and A[s] != A[s+1]:
            res.append(s+1)
        s += 1
        e += 1
    print("centers",res)











if __name__ == '__main__':

    A = [0, 0, 0, 1, 1, 0, 1]
    B = 0 

    # A = [1, 0, 1, 0, 1]
    # B = 1 
    print(AlternateSubArrayB(A,B))