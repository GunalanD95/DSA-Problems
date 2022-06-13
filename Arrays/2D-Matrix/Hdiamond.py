'''
Write a program to input an integer N from user and print hollow diamond star pattern series of N lines.

See example for clarifications over the pattern.

Output 1:

********
***  ***
**    **
*      *
*      *
**    **
***  ***
********
'''
def PrintDia(A):
    N  = A
    for i in range(N,0,-1):
        for j in range(i,0,-1):
            print("*",end="")

        # for space
        for k in range((N-i)*2):
            print(" ",end="")

        for j in range(i,0,-1):
            print("*",end="")

        print()

    for j in range(N):
        for i in range(j+1):
            print("*",end="")

        for k in range((N-j-1)*2):
            print(" ",end="")


        for k in range(j+1):
            print("*",end="")
        print()





if __name__ == '__main__':
    A = 5
    print(PrintDia(A))