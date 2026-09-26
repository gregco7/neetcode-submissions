#more practical + clean solution (Neetcode)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) - 1

        while l <= r:
            #addressing edge case where swap is between last/first
            
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1 #if m less than L, go right
            else:
                r = m - 1
            
        return res
        