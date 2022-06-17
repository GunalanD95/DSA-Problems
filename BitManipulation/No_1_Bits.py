'''
Write a function that takes an integer and returns the number of 1 bits it has.

'''


def Noof1bits(A):

    # implement divmod function to get the quotient and remainder

    def checkith(n,i):
        mask = 1 << i
        if n & mask > 0:
            return 1
        else:
            return 0
        
    c = 0
    for i in range(32):
        val = checkith(A,i)
        if val == 1:
            c += 1
            
    return c


# Approach :
# 1. Use the mask to check if the bit is 1 or 0
# 2. If the bit is 1, increment the count
# 3. Return the count


if __name__ == '__main__':
    A = 11
    print(Noof1bits(A))