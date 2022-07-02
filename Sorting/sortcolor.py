'''
Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

Note: Using the library sort function is not allowed.
'''

# Dutch National Flag Problem

def sortColors(A):
    l = 0
    m = 0
    h = len(A) - 1

    while m <= h:
        if A[m] == 1:
            m += 1
            
        elif A[m] == 0:
            temp = A[m]
            A[m] = A[l]
            A[l] = temp
            m += 1
            l += 1
            
        elif A[m] == 2:
            temp1 = A[m]
            A[m] = A[h]
            A[h] = temp1 
            h -= 1
    return A

# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach :
# 1. Create three pointers, l, m, h
# 2. l = 0, m = 0, h = len(A) - 1
# 3 . run a loop while m <= h till m is not equal to h
# 4 . we need to check if A[m] == 1 then m += 1
# 5 . if A[m] == 0 then we need to swap A[m] and A[l]
# 6 . if A[m] == 2 then we need to swap A[m] and A[h]
# 7 . m += 1, l += 1, h -= 1




if __name__ == '__main__':
    A = [0 ,1 ,2 ,0, 1, 2]
    print(sortColors(A))