'''
Sort the array using Quick Sort

Quick Sort --> Work by rearranging the index values to its corrected position 
by doing recursviely we can sorted each index value till it becomes sorted 

'''
from random import randint
class QuickSort():

    def Rearrange(self,arr,start,end):
        pivot = start

        start += 1

        while start <= end:

            if arr[start] <= arr[pivot]:
                start += 1

            elif arr[end] > arr[pivot]:
                end -= 1

            else:
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp 
                start += 1
                end -= 1


        arr[pivot] , arr[start-1] = arr[start-1] , arr[pivot]

        return start-1


    def QuickSort(self,arr,start,end):

        if start >= end:
            return 

        pivot = randint(start, end) # generate random pivot index and swap with A[start] for randomized pivot
        arr[pivot], arr[start] = arr[start], arr[pivot]

        index = self.Rearrange(arr,start,end)
        self.QuickSort(arr, start  , index - 1)
        self.QuickSort(arr, index + 1, end)


    def solve(self,A):

        self.QuickSort(A,0,len(A)-1)
        return 




if __name__ == '__main__':
    A = [4,75,43,13,32,99,2,1,0]
    # A = [ 1, 4, 10, 2, 1, 5 ]
    A = [2,1]


    quick = QuickSort()
    
    quick.solve(A)
    print("A",A)