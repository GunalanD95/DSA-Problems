'''
You have an array A with N elements. We have two types of operation available on this array :
We can split an element B into two elements, C and D, such that B = C + D.
We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
You have to determine whether it is possible to convert array A to size 1, containing a single element equal to 0 after several splits and/or merge?
'''


# 1) Xor Sum Approach:

def XorZero(A):
    op = 0
    for i in range(len(A)):
        op ^= A[i]
            
    if op % 2 == 0:
        return("Yes")
    else:
        return("No")


# Approach  :
# 1) Xor all the elements in the array.
# 2) If the Xor is even, then it is possible to convert the array to size 1, containing a single element equal to 0.
# 3) If the Xor is odd, then it is not possible to convert the array to size 1, containing a single element equal to 0.



if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    print(XorZero(A))