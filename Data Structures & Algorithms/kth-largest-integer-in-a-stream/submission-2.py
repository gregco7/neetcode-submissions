class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums,k
        heapq.heapify(self.heap)

        # heap pop till lenght matches k
        # whats left should be the kth largest element
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int: 
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]



