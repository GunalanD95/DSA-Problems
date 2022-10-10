'''
Given a Queue Q containing N elements. 
The task is to reverse the Queue. 
Your task is to complete the function rev(), that reverses the N elements of the queue.

'''

#User function Template for python3

#Function to reverse the queue.
import queue 
def rev(q):
    #add code here
    stack = []
    
    while q.qsize() != 0:
        ele = q.get()
        stack.append(ele)
     
    while stack:
        ele = stack.pop()
        q.put(ele)
        
    return q



q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
print("rev",rev(q))

