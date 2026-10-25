class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist (x: List[int]) -> int:
            return math.pow(x[0],2) + math.pow(x[1],2)
        
        # minheap: pop the smallest
        # maxheap: pop the largest

        # a max heap containing the smallest k integers
        # construct a max heap from tuples (dist, i)

        # pop until u just have k left, this should be the smallest k
        # return those guys

        maxHeap = [(dist(v),i) for i,v in enumerate (points)]
        heapq.heapify(maxHeap)
        res = []
        
        while k > 0:
            res.append(points[(heapq.heappop(maxHeap))[1]])
            k -= 1
        
        return res

