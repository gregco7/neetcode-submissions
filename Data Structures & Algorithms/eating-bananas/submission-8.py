class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # given an integer array piles
        # where piles[i] is the number of bananas in the ith pile
        # you are also given an integer `h` which represents the number
        # of hours you have to eat all the bananas.

        # you may decide your banas-per-hour eating of k. Each hour, you may
        # choose a pile of bananas and eat `k` bananas from that pile

        # if the pile has less than `k` bananas, you may finish eating
        # the pile but you can not eat from another pile in the same hour.

        # return the minimum integer k such that you can eat all the banas within `h`
        # hours

        # O(nlogm) time, 0(1) space ideal

        # checks if a result schema works in O(n)

        def check (rate:int):
            return sum((p + (rate - 1)) // rate for p in piles ) <= h
        
        l,r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            if check(m):
                # left half
                r = m
            else:
                # right half
                l = m + 1
        
        return l



