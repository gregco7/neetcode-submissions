class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index,value in enumerate(nums):

            #skip duplicate targets
            if index > 0 and value == nums[index-1]:
                continue

            l,r = index + 1, len(nums) - 1

            # main O(n^2) problem solving loop, two sum using two pointers
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum < 0: #too small, increase by incrementing left pointer
                    l += 1
                elif threeSum > 0: #too big, decrease by decrementing right pointer
                    r -= 1
                else: #valid triple
                    result.append([value,nums[l],nums[r]])
                    l += 1
                    #increment left pointer until it != what it already was, another 'no duplicate' insurance
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return result

            
    
                
            
            



        