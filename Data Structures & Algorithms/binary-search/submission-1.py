class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums) - 1 # 3 --> 0 (1) 2 | 4 -> 0 1 (2) 3
        m = l + ((r-l) //2)

        while (nums[m] != target) and (m != r) and (m != l):
            
            if nums[m] < target:
                # shrink to right half
                l = m
            else:
                #shrink to left half
                r = m
            
            m = l + ((r-l) //2)

        if nums[m] == target:
            return m
        elif nums[r] == target:
            return r
        else:
            return -1