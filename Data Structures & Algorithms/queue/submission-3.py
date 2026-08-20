#So I am going to try to implement this queue class
#using a single linked list, with enqueue and dequeue times in O(1) time complexity.

#List nodes will be implemented in the val,next format

class listNode:

    # [prev,value, next]

    def __init__(self,value: int,prev=None,next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return (not self.tail)

    def append(self, value: int) -> None:
        #Follow FIFO principles: Queue operation adds to the end.
        new_node = listNode(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def appendleft(self, value: int) -> None:
        #Flex FIFO principles: Queue adds to the beginning
        new_node = listNode(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        elif self.head == self.tail:
            our_val = self.head.value
            self.head = None
            self.tail = None
            return our_val
        else:
            our_val = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            return our_val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        elif self.head == self.tail:
            our_val = self.head.value
            self.head = None
            self.tail = None
            return our_val
        else:
            our_val = self.head.value
            self.head = self.head.next
            self.head.prev = None
            return our_val
