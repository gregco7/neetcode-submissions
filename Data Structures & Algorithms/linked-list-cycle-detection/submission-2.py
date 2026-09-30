# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        drag,front = head,head

        while front and front.next:

            drag = drag.next
            front = front.next.next

            # If this condition is fulfilled, its because front is looping drag.
            # This can only occur when there is a loop. 
            # Therefore we return true

            if drag == front:
                return True
        
        # Otherwise, the loop terminates meaning a .next is NULL somewhere and the linkedlist
        # Is accyclic.
        return False
        

        