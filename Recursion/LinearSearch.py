# Linear Search Return List W/O Passing as Argument





def findAllIndex(arr,indx,target):
    # for each call we are creating a new array
    ans = []

    # base condition
    if indx == len(arr):
        return  ans

    if arr[indx] == target:
        ans.append(indx)


    find_All = findAllIndex(arr,indx+1,target)

    print("find_All",find_All,ans)
    if find_All:
        ans.extend(find_All)

    return ans






#######1###3#4
A = [1,6,5,6,6]

print("Ans:",findAllIndex(A,0,6))