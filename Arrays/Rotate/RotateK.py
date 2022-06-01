'''
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
'''


# 1) Optimal Approach:

def rotate(A,B):
    """
    Do not return anything, modify nums in-place instead.
    """
    N = len(A) - 1
    
    def Rev(A,st,end):
        s = st
        e = end
        
        while s <= e:
            temp = A[s]
            A[s] = A[e]
            A[e] = temp
            
            s += 1
            e -= 1
        return A
            
    revA = Rev(A,0,N)
    print("Reversed Array:",revA)
    rev0B = Rev(revA,0,B-1)
    print("Reversed Array from 0 to B:",rev0B)
    RevRes = Rev(rev0B,B,N)
    print("Reversed Array from B to N-1",RevRes)




if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(rotate(nums,k))
