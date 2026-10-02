# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s,f = head,head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        # break the link between first & second half
        second = s.next
        s.next = None

        # reverse second half

        prev = None
        while second:
            nxt = second.next 
            second.next = prev 
            prev = second 
            second = nxt
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2
            










        