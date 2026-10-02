# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        toRemove = count - n

        if count == 1: return None;
        if toRemove == 0: return head.next

        start = head
        for i in range(toRemove):

            if i == toRemove - 1:
                start.next = start.next.next 
                break
            start = start.next

        return head