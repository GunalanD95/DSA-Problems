'''
Given two binary strings, return their sum (also a binary string).

'''

def AddBinaryStrings(A,B):
    # converting to ints
    A = list(A)
    B = list(B)

    A = [int(i) for i in A]
    B = [int(j) for j in B]

    N = len(A)
    M = len(B)


    # if one of the strings is longer than the other, we need to pad the shorter one with zeros
    if N !=  M:
        if N > M:
            while M < N:
                B.insert(0,0)
                N = len(A)
                M = len(B)
        else:
            while N < M:
                A.insert(0,0)
                N = len(A)
                M = len(B)


    # adding the binary strings together

    s = len(A) - 1
    res = list(range(N))
    car = 0
    while s >= 0:
        # using mod and div to get the carry and calculate the sum
        sum = A[s] + B[s] + car
        res[s] = (sum) % 2
        car = (sum) // 2

        s -=  1

    # if the carry is 1, we need to add it to the result

    if car == 1:
        res.insert(0,1)


    # converting the result to a string
    return "".join(str(i) for i in res)





if __name__ == '__main__':
    A = "100"
    B = "11"   

    # A = "1"
    # B = "001"

    A = "1"
    B = "111"

    # A = "11"
    # B = "1"

    print(AddBinaryStrings(A,B))