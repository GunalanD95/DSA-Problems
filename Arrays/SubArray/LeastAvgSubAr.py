import sys

'''
Problem Description
Given an array of size N, find the subarray of size K with the least average.

A=[3, 7, 90, 20, 10, 50, 40]
B=3
10+50+40 = 100/ B = 33 [ LEAST AVG ]

Hey, just remove //B from line 26 because decimal numbers when treated as integers gives erros.

You know we have to find index of min average subarray. since length of subarray is fixed so , min average means min sun subarray.

so just compare using sum.
'''





def FindAverage(A,B,N):
    def createPF(A,N):
        PF = list(range(0,N))
        PF[0] = A[0]
        for i in range(1,N):
            PF[i] = PF[i-1] + A[i]
        return PF

    PF = createPF(A,N)

    s = 0
    e = B - 1


    res =  sys.maxsize
    out = N
    while e < N: 
        if s == 0:
            avg = PF[e]
        else:
            avg = PF[e] - PF[s-1]
        avg = avg 
        if avg < res:
            res = avg
            out = s
        
        s += 1
        e += 1
    return out 

if __name__ == '__main__':
    # A=[3, 7, 90, 20, 10, 50, 40]
    # B=3

    A = [ 18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19 ]
    B = 1

    # A = [ 15, 7, 11, 7, 9, 8, 18, 1, 16, 18, 6, 1, 1, 4, 18 ]
    # B = 6
    

    A = [ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ]
    B = 9

    N = len(A)


    FindAverage(A,B,N)