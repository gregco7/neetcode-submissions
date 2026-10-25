class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)

        # Just keep the top k.
        # Of a min heap comprised of the largest k ints
        # Of the available nums
        # the root will be the kth largest integer.

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        heapq.heappush(self.heap,val)

        # if we overflow over the top k
        # pop to go back down to k
        # you could even while loop this, but its unnecessary
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
