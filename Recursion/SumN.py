# Recursion Definition:
#   A function that calls itself is called a recursive function.
#   A recursive function is a function that calls itself.

# Steps to write a recursive function:
# 1. write the main logic
# 2. write the base case
# 3. write the recursive case

def Sum(N):
    if N == 1:
        return 1

    return Sum(N-1) + N




if __name__ == '__main__':
    N = 5
    print(Sum(N))