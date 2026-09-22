class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ourMap = {}

        for index,num in enumerate(nums):

            neededNumber = target - num

            if neededNumber in ourMap:
                return [ourMap[neededNumber],index]
            else:
                ourMap[num] = index

        return []

       