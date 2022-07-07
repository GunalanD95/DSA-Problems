def getbinary(number):
   
    # Base case
    if number == 0:
        return 0
       
     # Recursion call and storing the result
    print("number",number)
    smallans = getbinary(number // 2)
    print("smallans",smallans)
    return number % 2 + 10 * smallans
       
       
N = 5
res = getbinary(N)
print("res",res)