'''
Given an integer A. Unset B bits from the right of A in binary.
For eg:-
A = 93, B = 4
A in binary = 1011101
A should become = 1010000 = 80. Therefore return 80.

Input 1:-
A = 25
B = 3

Input 2:-
A = 37
B = 3

Output 1:-
24

Output 2:-
32

'''



def solve(A, B):
    return (A  & (~0 << B))



if __name__ == '__main__':
    A = 25 
    B = 3

    A = 37
    B = 3
    print(solve(A,B))



# To unset bits we need to use &(AND) operation with the given number, A using zeros.

# but we are asked only to unset B number of bits from the right. So, we should have the B bits from the right as zero(0) and the rest as one (1).
# In order for that, 
# negate the zero (~0 = 1111111111111...11111)
# Now left shit the above value with B ( ex. ~0 << 4 = 11111111.....11110000)
# Now perform the &(AND) operation between the above-generated result and A. 
# Let's suppose A = 1011101
# B = 4
# ~0 = 1111111
# ~0<<B = ~0 << 4 = 1110000
# A & (~0 << B) => 
#      1 0 1 1 1 0 1
#   &  1 1 1 0 0 0 0
# --------------------------------
#      1 0 1 0 0 0 0 

# So result is 80 