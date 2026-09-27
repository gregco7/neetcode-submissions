class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            # Remove negative prefixes
            if curSum < 0:
                curSum = 0
            # Add next value and update max sum
            curSum += num
            maxSum = max(maxSum,curSum)
        return maxSum