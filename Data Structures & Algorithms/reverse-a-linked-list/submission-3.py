# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.





"""

#My old iterative Solution: T: O(n), M: O(1) linear time complexity, constant memory complexity

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            #Need to return tail with proper chain
            
            prev = head # 0
            curr = head.next # 1

            head.next = None

            while curr: # 1, # 2
                original_pointer = curr.next # 2, # 3
                curr.next = prev # 1 -> 0, 2 -> 1

                prev = curr # 1
                curr = original_pointer # 2
            
            return prev
        else:
            return None
"""

#Now solve recursively, his style from memory

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next) # 2
            head.next.next = head

        head.next = None
        return newHead

        

        
        
        