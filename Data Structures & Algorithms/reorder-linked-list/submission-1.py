# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Initialize Slow & Fast Pointers to divide the LinkedList into two halves
        # Incrementing slow by 1 point and fast by two points iteratively
        # No extra memory needed

        s,f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        second = s.next
        s.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # merge two halfs 
        # second half could be potentially smaller so that 
        # will be our loops stopping point

        first, second = head,prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first,second = tmp1, tmp2







        