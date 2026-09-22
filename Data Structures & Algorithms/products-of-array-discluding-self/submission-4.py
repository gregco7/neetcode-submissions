class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        prefixNum = 1
        for i in range(len(nums)):
            result[i] = prefixNum
            prefixNum *= nums[i]

        postfixNum = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfixNum
            postfixNum *= nums[i]
        return result


        



        



        