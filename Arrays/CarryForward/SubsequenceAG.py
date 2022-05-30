A = "ABCGAG"

'''Problem :
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.
'''

#1-  BruteForce Approach 

def subsequence(A):
    N = len(A)
    count = 0
    for i in range(N):
        ele = A[i]
        if ele == "A":
            for j in range(i+1,N):
                if A[j] == 'G':
                    count += 1
                    # break

    print(count)
        
# Time Complexity: O(N)2
# Space Complexity: O(1)




#2- Optimized Approach -  A = "ABCGAG"

def subsequence(A):
    N = len(A)
    ans = 0
    N_As = 0
    for i in range(N):
        ele = A[i]
        if ele == 'A':
            N_As += 1
        elif ele == 'G':
            ans = ans + N_As

    print(ans)


# Time Complexity - O(N)
# Space Complexity - O(1)



if __name__ == '__main__':
    A = "ABCGAG"
    subsequence(A)