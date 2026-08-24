#Implementation of a doubly list node
class listNode:

    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
#Implement the scope of the problem using a dummy node to reduce edge case fulfillment requirements.
class MyLinkedList:

    def __init__(self):
        dummyHead = listNode(-1)
        dummyTail = listNode(-1)

        self.head = dummyHead #Perma Head
        self.tail = dummyTail #Perma Tail

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        while (curr != self.tail and index > 0):
            curr = curr.next
            index -= 1
            
        if (curr != self.tail and index == 0):
            return curr.val
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:
        # Initialize new Head to be just after dummy head.
        newNode = listNode(val) 

        #Forward Pointers
        newNode.next = self.head.next 
        self.head.next = newNode 

        #Backward Pointers
        newNode.next.prev = newNode
        newNode.prev = self.head

    def addAtTail(self, val: int) -> None:
        # Initialize new Tail to be just before dummy tail.
        newNode = listNode(val) 

        #Forward Pointers
        newNode.next = self.tail
        self.tail.prev.next = newNode

        #Backward Pointers
        newNode.prev = self.tail.prev
        self.tail.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = listNode(val)

        curr = self.head
        while (curr.next and index > 0):
            curr = curr.next
            index -= 1
        
        if (curr.next and index == 0):
            #Forward Pointers
            newNode.next = curr.next
            curr.next = newNode

            #Backward Pointers
            newNode.next.prev = newNode
            newNode.prev = curr

    def deleteAtIndex(self, index: int) -> None:
        
        #For a deletion to be valid, the selected node must have a .next and a .prev due to dummy logic
        #After the loop, curr should equal the node to be removed.
        curr = self.head.next

        while (curr.next and index > 0):
            curr = curr.next
            index -= 1
        
        if (curr.next and index == 0):
            #Forward and Backward pointers 
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            #This might help with deallocating this listNode
            curr.next = None
            curr.prev = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)