# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newHead = ListNode(-1) #Dummy Node
        pointer = newHead

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    pointer.next = list1
                    pointer = list1
                    list1 = list1.next
                else:
                    pointer.next = list2
                    pointer = list2
                    list2 = list2.next
            elif list1:
                pointer.next = list1
                pointer = list1
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = list2
                list2 = list2.next
        
        return newHead.next


        