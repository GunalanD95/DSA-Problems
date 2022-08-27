from functools import cache , lru_cache


# @cache
@lru_cache(maxsize=None)
def Fib(N):
    if N <= 1:
        return N

    return Fib(N-1) + Fib(N-2)


def main():
    for i in range(401):
        print("i",i,Fib(i))

    print("done")

A = [2,4,5,6,7]
A.sort()


if __name__ == '__main__':
    # N = 300
    # print(Fib(N))
    main()