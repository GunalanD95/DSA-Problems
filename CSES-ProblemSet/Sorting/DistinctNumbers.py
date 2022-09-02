def DistinctNumbers(A):
    A.sort()
    count = 1
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            count += 1

    print(count)



if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))
    DistinctNumbers(A)