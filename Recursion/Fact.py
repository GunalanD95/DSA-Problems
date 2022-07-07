
def Fac(N):
    if N == 0 or N == 1:
        return 1

    return N * Fac(N-1)


if __name__ == '__main__':
    N = 5
    print(Fac(N))