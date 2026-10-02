# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # given the head of a singly linked-list
        # re roder the nodes of the linked list like
        # [0, n-1, 1, n-2, 2, n-3]

        ourArr = []

        while head:
            ourArr.append(head)
            head = head.next

        head = ourArr[0]
        listLen = len(ourArr)
        
        # O (n)

        
        for i in range(listLen-1):
            #odd indexes get n - math.ceil (i/2)
            #even indexes get i / 2

            #listLen - 1 gets .next = none

            if (i % 2 == 0):
                head.next = ourArr[listLen - math.ceil( (i+1)/2 )]
            else:
                head.next = ourArr[math.ceil (i/2)]
            
            head = head.next
        
        head.next = None





        