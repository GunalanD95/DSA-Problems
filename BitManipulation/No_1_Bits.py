'''
Write a function that takes an integer and returns the number of 1 bits it has.

'''


def Noof1bits(A):

    # implement divmod function to get the quotient and remainder

    def divmod(a, b):
        return a // b, a % b

    no_of_1s = 0

    while A  > 0:
        A , rem = divmod(A, 2)
        if rem == 1:
            no_of_1s += 1

    return no_of_1s




if __name__ == '__main__':
    A = 44
    print(Noof1bits(A))