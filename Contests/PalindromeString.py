def isPalindrome(A):
    A = A.lower()
    s = len(A) - 1
    res = ''
    for i in range(len(A)):
        if A[i].isalnum():
            res = res + A[i]
            
    ans = ''
    while s >= 0:
        if A[s].isalnum():
            ans = ans + A[s]
            
        s -= 1
        
    if ans == res:
        return 1
    else:
        return 0


# Approach :
# 0. Convert the string to lowercase.
# 1. loop through the string and check if the character is alphanumeric.
# 2. If it is, append it to the ans string.
# 3. Reverse the ans string.
# 4. If the ans string is equal to the original string, return 1.
# 5. Else return 0.

# Complexity :
# Time : O(n)
# Space : O(n)



if __name__ == '__main__':
    A = "A man, a plan, a canal: Panama"
    print(isPalindrome(A))
