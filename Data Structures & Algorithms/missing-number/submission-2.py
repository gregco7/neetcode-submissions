class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # given an array nums containing n integers in the range [0,n]
        # without any duplicates, return the single number in the range
        # missing from nums.

        length = len(nums)

        big = (sum (range(length + 1)))

        for num in nums:
            big -= num

        return big