class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        presentSet = set()

        for num in nums:
            if num in presentSet:
                return True
            else:
                presentSet.add(num)

        return False
        