'''
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.

A = [1, 2, 3, 4, 5]
B = 4

o/p = 6

explanation :
Even length good subarrays = {1, 2} - 1
Odd length good subarrays  = {1, 2, 3}, {1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4, 5}, {5} - 5

'''

# 1 - Brute Force Approach

def CountGoodSubarryB(A,B):
    N = len(A)
    count = 0
    for i in range(N):
        sum = 0
        length = 0 
        for j in range(i,N):
            sum += A[j]
            # length = len(range(i,j)) + 1
            length  += 1
            print("sum:",sum,"len:",length,"i:",i,"j:",j)
            if length%2 == 0 and sum < B:
                count +=1
            elif length%2 != 0 and sum > B:
                count +=1
    return count
    


    
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 4

    A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
    B = 65

    print(CountGoodSubarryB(A,B))