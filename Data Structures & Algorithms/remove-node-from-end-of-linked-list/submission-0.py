# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # given head of linked list and integer n 
        # remove the nth node from the end of the list
        # and return its head

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        # now we have length and curr at the end of the list, # O(n)

        toRemove = count - n
        print(count, toRemove)

        if count == 1: return None;
        if toRemove == 0: return head.next

        start = head
        for i in range(toRemove):

            if i == toRemove - 1:
                print(i, start.val)
                start.next = start.next.next # could Be None, or the node after to be removed.
                break
            
            start = start.next

        return head



        return head