class Solution:
    #rotate means to shift everything up 1?
    #rotating means moving the last n elements to the beginning of the array
    #all nums unique
    #need to find solution in O(log n) time
    def findMin(self, nums: List[int]) -> int:

        l,r = 0, len(nums)-1
        m = r // 2

        while l < r:

            if (nums[m]==nums[l]) or (nums[m]==nums[r]) or (nums[l] < nums[r]):
                return min(nums[l],nums[r])

            if nums[m] > nums[l]:
                #go right, recalculate m 
                l = m
                m = ((r-l) // 2) + l
            else:
                #go left, recalculate m
                r = m
                m = ((r-l) // 2) + l
        
        return min(nums[l],nums[r])



        
        




        