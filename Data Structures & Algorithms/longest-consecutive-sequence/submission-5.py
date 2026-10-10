class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ourset = set(nums)
        res = 0

        for n in ourset:
            if n-1 in ourset:
                continue
            
            streak = 1
            while (n + 1) in ourset:
                streak += 1
                n += 1
            res = max(streak,res)
            
        
        return res

            