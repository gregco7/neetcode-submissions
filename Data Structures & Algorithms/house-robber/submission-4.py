class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # OPT (i), i > 1: = max (opt(i-2)+nums[i],opt(i-1))
        # i = 0: nums[0], i = 1: max(nums[1],nums[0])

        cache = [-1] * len(nums) # DUMMY PLACEMENTS

        def opt(i):

            if cache[i] != -1:
                return cache[i]

            if i > 1:
                cache[i] = max(opt(i-2)+nums[i],opt(i-1))
                return cache[i]
            elif i == 1:
                cache[i] = max(opt(0),nums[i])
                return cache[i]
            else:
                cache[i] = nums[i]
                return cache[i]
        
        return opt(len(nums)-1)