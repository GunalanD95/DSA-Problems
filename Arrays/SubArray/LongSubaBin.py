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
        e1 = 0 
        res = 0
        no_1s = 0
        # count the number of 1s in the array
        for i in range(N):                                   # loop through the array to count the number of 1s
            if A[i] == '1':
                no_1s += 1

        while end_indx <= N-1:                          # loop through the array to find the longest consecutive 1s
            length = 0 
            o_s = 0                                     # o_s is the number of 0's in the current subarray
            e1 = st_indx                                # e1 is the index of the last 1 in the current subarray
            length  = 0
            while e1 <= N-1:            
                if A[e1] != '1':                        # if the element is 0, increment the number of 0's in the current subarray
                    if o_s < 1:                         # if the number of 0's is less than 1, increment the length of the current subarray
                        o_s += 1
                        length += 1
                    else:
                        break
                elif A[e1] == '1':                      # if the element is 1, increment the length of the current subarray
                    length += 1
                e1 += 1
            res_len = max(length,res_len)               # find the longest consecutive 1s in the array

            st_indx  += 1
            end_indx += 1

        if res_len > no_1s:                                 # if the longest consecutive 1s is greater than the number of 1s in the array, return no_1s
            return(no_1s)
        else:
            return(res_len)                                 # else return the longest consecutive 1s in the array




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

