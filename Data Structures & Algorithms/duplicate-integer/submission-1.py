class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nSet = set()
        for num in nums:
            if num in nSet:
                return True
            nSet.add(num)
        return False
        