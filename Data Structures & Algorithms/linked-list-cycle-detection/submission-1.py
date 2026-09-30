# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        listNodeSet = set()

        while head:
            head = head.next
            if head in listNodeSet:
                return True
            listNodeSet.add(head)
        
        return False
        

        