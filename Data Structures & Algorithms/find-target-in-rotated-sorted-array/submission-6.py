class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
    
            if (nums[m] > nums[l]):
                if nums[l] <= target <= nums[m-1]:
                    r = m - 1
                else:
                    l = m + 1
            elif (nums[m] < nums[l]):
                if nums[m+1] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif (nums[r] == target):
                return r
            else:
                break

        return -1