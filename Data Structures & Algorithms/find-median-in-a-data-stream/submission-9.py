class MedianFinder:

    # the median is the middle value in a sorted list of integers
    # for lists of even length, there is no middle value,
    # and thus the median is the mean of the two middle values

    # ex 1: [1,2,3] -> 2
    # ex 2: [1,2] -> 1.5

    # implement the MedianFinder class
    
    # MedianFinder() initializes the MedianFinder object

    # void addNum (int num) adds the integer num from the data stream to the
    # data structure

    # double findMedian returns the median of all elements so far.


    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        # O(logn) time for addNum
        # make sure all nums in max heap are <= numbers in min heap
        if not self.maxheap:
            heapq.heappush(self.maxheap,-1 * num)
        elif not self.minheap:
            maxval = -1 * self.maxheap[0] 
            if num < maxval: 
                heapq.heappush(self.minheap, -1 * heapq.heappop(self.maxheap))
                heapq.heappush(self.maxheap, -1 * num)
            else:
                heapq.heappush(self.minheap, num)
        else:
            # insert
            maxval = -1 * self.maxheap[0]
            if maxval > num:
                heapq.heappush(self.maxheap,-1 * num)
            else:
                heapq.heappush(self.minheap,num)

        # correct
        while abs(len(self.maxheap) - len(self.minheap)) > 1:
            minL,maxL = len(self.minheap), len(self.maxheap)
            if maxL < minL:
                heapq.heappush(self.maxheap, -1 * heapq.heappop(self.minheap))
            else:
                heapq.heappush(self.minheap, -1 * heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        # O(1) time for findMedian
        minL, maxL = len(self.minheap) , len(self.maxheap)
        leng = minL + maxL

        if (leng % 2) == 1:
            if minL > maxL:
                return self.minheap[0]
            else:
                return -1 * self.maxheap[0]
        else:
            return (self.minheap[0] + (-1 * self.maxheap[0])) / 2
        