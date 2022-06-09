'''
You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.

You are to choose 3 trees such that their total cost is minimum. Return that cost.

If it is not possible to choose 3 such trees return -1.
'''

# 1) Brute Force


def MinTreeSum(A,B):
    N = len(A)

    def createPF(A,N):
        PF = list(range(0,N))
        PF[0] = A[0]
        for i in range(1,N):
            PF[i] = PF[i-1] + A[i]
        return PF

    PF = createPF(B,N)
    print("PF",PF)


    indx_range = tuple()
    st_indx = 0
    end_indx = 0    

    # for i in range(N):
        
        
        


    indx_range = st_indx , end_indx
    print("range",indx_range)

    
            


















if __name__ == '__main__':
    A = [1, 3, 5]
    B = [1, 2, 3]
    B =  [1, 6, 4, 2, 6, 9]
    A = [1, 6, 4, 2, 6, 9]

    print(MinTreeSum(A,B))