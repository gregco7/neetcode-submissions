class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # use python heapq
        self.heap, self.k = nums,k
        heapq.heapify(self.heap) # min heap of whole list
        # now pop() / remove root to get rid of smallest in the min heap
        # until we have just k elements left.
        # the root of that min heap, will be the smallest of the largest k ints
        # of the original nums list.
        # thus being the kth largest integer.

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

