# Q1 - Find Nth Fibonacci Number :


def fibo(num):

    # Base Condition
    if num == 0 or num == 1:
        return num 

    # Logic 
    return fibo(num-1) + fibo(num-2)




print("fibo",fibo(4))