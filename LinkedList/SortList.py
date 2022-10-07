# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if not list1 and list2: return None 
        
        # using merge function from merge sort
        list1 = None
        tail = None 
        if list1.val <= list2.val:
            h3 = list1
            list1 = list1.next
            tail = list1
            list2 = list2
        else:
            list1 = list2
            list1 = list1.next
            tail = list1
            list2 = list1
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                
                
        list1.next = None        
                
        print("list1",list1)






                
                
                
                
        
        
        
        
        
        