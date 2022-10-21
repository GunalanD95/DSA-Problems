# take a number as input and prints it 
# print first five numbers :1 2 3 4 5 


def printFun(num):
    print("num is:",num)
    printFun2(num+1)

def printFun2(num):
    print("num is:",num)
    printFun3(num+1)

def printFun3(num):
    print("num is:",num)
    printFun4(num+1)

def printFun4(num):
    print("num is:",num)
    printFun5(num+1)


def printFun5(num):
    print("num is:",num)

printFun(1)