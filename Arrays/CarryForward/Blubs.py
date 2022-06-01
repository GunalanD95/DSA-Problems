'''
A wire connects N light bulbs.

Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.
'''

# 1) BruteForce Approach ( Will Fail - TLE )

def TurnOn(A):
    N = len(A)
    
    c =  0
    find = 0
    for i in range(N):
        if A[i] == find:
            c += 1
        if find == 0:  
            find = 1
        else:
            find == 0

    print(c)

# Time Complexity: O(N^2)
# Space Complexity: O(1)























if __name__ == '__main__':
    A = [0, 1, 0, 1]
    A = [0,1,0,1]
    A = [1,1,1,1]
    TurnOn(A)