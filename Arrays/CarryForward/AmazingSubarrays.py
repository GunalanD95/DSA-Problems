'''
You are given a string S, and you have to find all the amazing substrings of S.

An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

'''

# 1) - Optimized Approach  


def SubArray(A):
    Vow = ['a','e','i','o','u','A','E','I','O','U']
    N = len(A)

    ans = 0
    for i in range(N):
        if A[i] in Vow:
            length = N - i
            ans += length
            
            
    return(ans % 10003)












if __name__ == '__main__':
    S = 'amazing'
    print(SubArray(S))