class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSort(l,r):
            pivotVal, p = nums[r],l

            for i in range (l,r):
                if nums[i] <= pivotVal:
                    nums[i],nums[p] = nums[p], nums[i]
                    p += 1
            nums[p],nums[r] = nums[r], nums[p]
            
            # left of p < pivotval
            # p = pivot val
            # right of p > pivotval

            if k > p: return quickSort(p + 1, r)
            if k < p: return quickSort(l, p - 1)
            return nums[p]

        return quickSort(0,len(nums)-1)