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

        def check (arr: List[int], maxHours: int, rate: int) -> bool:
            for n in arr:
                maxHours -= math.ceil(n / rate)

            if maxHours > -1:
                return True
            return False

        l, r = 1, max(piles)
        m = math.ceil((l + r) / 2)

        while r > 2 :
            curr = check(piles,h,m)
            adjacent = check(piles,h,m-1)

            if ((not curr) and adjacent):
                return m-1
            elif (curr and (not adjacent)):
                return m
            elif not curr:
                # go to right half
                l = m
                m = math.ceil((l + r) / 2)
            else:
                # go to left half
                r = m
                m = math.ceil((l + r) / 2)
            
        return 1 if check(piles,h,1) else 2






