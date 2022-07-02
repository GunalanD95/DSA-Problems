
def Nof1Bits(A):      
    c = 0
    for i in range(32):  
        if (1 << i) & A > 0:
            c += 1   
    return c


# Approach :
# 0 . We need to find the number of 1 bits in the given number of int range(32) .
# 1. Use the bitwise operator to check if the bit is set or not.  1 << i will give the value of the bit at position i.
# 2. If the bit is set, increment the count.
# 3. Return the count.

#  Complexity :
#  Time : O(1)
#  Space : O(1)

if __name__ == '__main__':
    A = 99
    print(Nof1Bits(A))