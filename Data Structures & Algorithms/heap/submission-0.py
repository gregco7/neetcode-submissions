# a min heap should always satify: parent <= child
class MinHeap:

    # helper funcs

    @staticmethod
    def parentIndex(i: int) -> int:
        return ((i-1)//2)
    
    @staticmethod
    def leftChild(i: int) -> int:
        return (2 * i) + 1
    
    @staticmethod
    def rightChild(i:int) -> int:
        return (2 * i) + 2

    def __init__(self):
        self.heap = []

    def heapifyDown(self,i):

        leng = len(self.heap)
        li = self.leftChild(i)
        ri = self.rightChild(i)

        while (li < leng):
            # if children are less than parent, swap them, if both less, swap with smaller child.
            l,r = self.heap[li], self.heap[ri] if ri < leng else float("infinity")
            val = self.heap[i]

            if not ((val > l) or (val > r)):
                break # min heap requirement satisfied

            # needs to swap with one of them
            if (r < l):
                # swap with right
                self.heap[ri], self.heap[i] = val, r
                i = ri
            else:
                #swap with left
                self.heap[li], self.heap[i] = val, l
                i = li

            # set new children
            li = self.leftChild(i)
            ri = self.rightChild(i)

    def push(self, val: int) -> None:
        # push it onto the last element, then heapify up.
        self.heap.append(val)
        
        # PARENT: i
        # LEFT CHILD: 2i + 1
        # RIGHT CHILD: 2i + 2

        i = len(self.heap) - 1
        while (i > 0 and self.heap[self.parentIndex(i)] > self.heap[i]):
            #switch
            self.heap[self.parentIndex(i)],self.heap[i] = self.heap[i],self.heap[self.parentIndex(i)]

            #set new index
            i = self.parentIndex(i)

    def pop(self) -> int:
        if len(self.heap) < 1:
            return -1
        popped = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1] # set the root value to the final leaf nodes value
        self.heap.pop()
        self.heapifyDown(0)

        return popped
        

    def top(self) -> int:
        if not self.heap:
            return -1
        else:
            return self.heap[0]

    def heapify(self, nums: List[int]) -> None:
        
        # heapify down from last non-leaf nodes
        self.heap = nums[:]
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            #heapify down
            self.heapifyDown(i)
        






        