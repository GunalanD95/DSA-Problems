# take a number as input and prints it 
# print first five numbers :1 2 3 4 5 


# N TO 1 

N = 5
    
# def printN(num):
#     if num == 1:
#         print(1)
#         return 
#     print(num)
#     printN(num-1)
   
# printN(5)


# 1 TO N 

def printN(num):
    if num == 1:
        print(1)
        return 
    printN(num-1)
    print(num)
   
printN(5)
