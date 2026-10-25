# given an array of integers stones where stones[i]
# represents the weight of the ith stone.
# run a simulation
# at each step we choose the two heaviest stones, with weigh x and y
# and smash them together
# case x == y : both are destroyed
# x < y, the stone of weight x is destroyed
# and the stone of weight y has new weight y - x


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-n for n in stones]
        heapq.heapify(stones) # max heap

        while len(stones) > 1:
           largest = heapq.heappop(stones)
           secondLargest = heapq.heappop(stones)

           if largest == secondLargest:
                continue
           else:
                heapq.heappush(stones,largest - secondLargest)

        return -stones[0] if len(stones) == 1 else 0