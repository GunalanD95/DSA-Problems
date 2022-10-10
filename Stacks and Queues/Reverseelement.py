'''
Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, leaving the other elements in the same relative order.

NOTE: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.


'''

import queue
A = queue.Queue()

from collections import deque
A.put(1)
A.put(2)
A.put(3)
A.put(4)
A.put(5)

ans = []
B = 3
for i in range(B):
    ele = A.get()
    print('ele-1',ele)
    ans.append(ele)

while ans:
    ele = ans.pop()
    A.put(ele)
    
length = A.qsize() - B
print("length",length)
    
while length != 0:
    ele = A.get()
    A.put(ele)
    length -=1


print("ans",A)
print(list(A.queue))
    