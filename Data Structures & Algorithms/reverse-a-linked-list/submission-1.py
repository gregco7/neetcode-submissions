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

#Now solve recursively, use dummy node

class Solution:

    def reverseList(self, head: Optional[ListNode],prev = None) -> Optional[ListNode]:

        #BASE CASE: No Head
        if not head:
            return None
        
        if head.next:
            LN = self.reverseList(head.next,head) #2,3
            head.next = prev # 3 --> 2
            return LN
        else:
            head.next = prev
            return head 
        
        