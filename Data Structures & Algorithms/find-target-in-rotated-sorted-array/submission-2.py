class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

        #elements of nums are unique

        #write an algorithm in O(log n) time

        l, r = 0,len(nums) - 1

        while l <= r:

            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            if (nums[m] > nums[l]):
                #left bound valid (L through m-1)
                if nums[l] <= target <= nums[m-1]:
                    #target in left bound, shrink to left half
                    r = m - 1
                else:
                    #not in left bound, shrink to right half
                    l = m + 1
            elif (nums[m] < nums[l]):
                if nums[m+1] <= target <= nums[r]:
                    #target in right bound, shrink to right half
                    l = m + 1
                else:
                    #not in right bound, shrink to left half
                    r = m - 1
            else:
                break

        return -1