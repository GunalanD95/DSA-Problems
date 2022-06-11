'''
Given a binary string A.
It is allowed to do at most one swap between any 0 and 1.
Find and return the length of the longest consecutive 1’s that can be achieved.

'''
import sys

def CountLongSubArrayB(A):
    A = list(A)
    N = len(A)


    
    res_len = -sys.maxsize - 1
    st_indx = 0
    end_indx  = st_indx + 1
    s1 , e1 = 0 , 0
    res = 0
    no_1s = 0
    # count the number of 1s in the array
    for i in range(N):
        if A[i] == '1':
            no_1s += 1
    if N <= 2:
        if N == 1:
            if A[st_indx] == '1':
                res += 1
        if N == 2:
            if A[end_indx] == '1':
                res += 1
        res_len = max(res,res_len)
    else:
        while end_indx <= N-1:
            length = 0 
            o_s = 0
            e1 = st_indx
            while e1 <= N-1:        
                if A[e1] != '1':
                    if o_s < 1:
                        print("zone",e1)
                        o_s += 1
                        length += 1
                    else:
                        break
                elif A[e1] == '1':
                    length += 1
                e1 += 1


            print("st_indx,end_indx",st_indx,end_indx)
            print("Length:",length)
            res_len = max(length,res_len)

            st_indx  +=  1
            end_indx += 1

    if res_len >= no_1s:
        print("ANSWER:",no_1s)
    else:
        print("ANSWER:",res_len)

    print("ANSWER:",res_len)




if __name__ == '__main__':

    # A = "111000"                      # O/P = 3
    A = "111011101"                   # O/P = 7
    # A = "010100110101"                # O/P = 4
    # A = "100001011"                   # O/P = 4 
    # A = "010100110101"                # O/P = 4
    # A = "1"                           # O/P = 1
    # A = "110011"                      # O/P = 3
    # A = "10011"                       # O/P = 3





    print(CountLongSubArrayB(A))

