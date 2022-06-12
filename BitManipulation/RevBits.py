'''
Reverse the bits of an 32 bit unsigned integer A.

'''

def Revbits(A):

    def divmod(a, b):
        return a // b, a % b

    def convertoBinary(A):
        # 32 bit list
        binary = [0] * 32
        rems = 0
        temp = 0
        while A > 0:
            A , rems = divmod(A,2)
            binary[temp] = rems 
            temp += 1
        return binary



    def rev(A):
        N = len(A)
        s = 0
        e = N -1 
        while s <= e:
            temp = A[s]
            A[s] = A[e]
            A[e] = temp
            s += 1
            e -=1
        return A

    def convertoDecimal(A):
        N = len(A)

        s = N - 1
        pow1 = 0
        total = 0
        while s >= 0:
            A[s] = A[s] * (2 **pow1)
            if A[s] != 0:
                total += A[s]
            pow1 += 1
            s -= 1 
        return total       

        



    binary = convertoBinary(A)
    print(binary)
    # binaryRev = rev(binary)
    return convertoDecimal(binary)





if __name__ == '__main__':
    A = 22
    print(Revbits(A))