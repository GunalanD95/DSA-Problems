
def Fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    return Fib(N-1) + Fib(N-2)








if __name__ == '__main__':
    N = 3
    print(Fib(N))