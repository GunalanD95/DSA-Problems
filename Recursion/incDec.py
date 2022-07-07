# Given a number print all the numbers from N to 1 in decreasing order


def Dec(N):
    print(N)
    if N == 1:
        return 
    return Dec(N-1)


def Inc(N):
    if N == 0:
        return
    Inc(N-1)
    print(N)


def bar(x,y):
    if y ==0:
        return 0
    return (x + bar(x,y-1))
    
def foo(x,y):
    if y ==0:
        return 1
    return bar(x,foo(x,y-1))
    
# print(foo(3,5))


def fun(x,n):
    if n ==0:
        return 1
    elif n % 2 == 0:
        return fun(x*x,n//2)
    else:
        return x * fun(x*x,(n-1)//2)

print(fun(2,10))



if __name__ == '__main__':
    N = 5
    # print(Inc(N))