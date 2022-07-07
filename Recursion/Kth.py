def findK(A, B):

    if A == 1 : return 0
    parent = findK(A-1,B//2 + B %2)

    bool = (B%2 == 1)

    if parent == 1:
        if bool:
            return 1 
        else: 
            return 0
    else:
        if bool:
            return 0 
        else: 
            return 1
       
       
A = 2
B = 2
res = findK(A,B)
print("res",res)