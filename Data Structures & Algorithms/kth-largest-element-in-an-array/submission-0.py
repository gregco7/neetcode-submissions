class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # min heap, then pop till ur at k?
        negNums = [-n for n in nums]
        heapq.heapify(negNums) # min heap

        while k > 1:
            heapq.heappop(negNums)
            k-=1
        
        return -heapq.heappop(negNums)

        