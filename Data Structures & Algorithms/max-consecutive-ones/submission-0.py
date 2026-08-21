class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max = 0
        curr = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            
            if curr > max:
                max = curr
        
        return max