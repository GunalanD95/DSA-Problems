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

    if B <= 0:
        return list(range(N))                  # If B is 0, return all the indices of the array
        
    B = 2 * B + 1                              # B is the length of the subarray


    res = []
    for i in range(N):                         # Iterate over the array
        s = A[i]                               # s is the current element
        count = 0                              # initialize count
        for j in range(i,min(i+B,N)):          # Iterate over the subarray of length B
            if s == A[j]:                      # If the element is same as the current element
                count += 1                     # Increment the count
            s = 1 - s                          # Flip the element to 1 - s , so that we can check the next element in the subarray

        if count == B:                         # If the count is equal to B, then we have found the alternate subarray
            res.append(i+B//2)
    return res  




if __name__ == '__main__':

    A = [0, 0, 0, 1, 1, 0, 1]
    B = 0 

    A = [1, 0, 1, 0, 1]
    B = 1 


    print(AlternateSubArrayB(A,B))