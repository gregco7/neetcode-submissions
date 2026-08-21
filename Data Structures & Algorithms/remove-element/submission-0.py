#I will leave the underscores as -1

class Solution:


    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        refurbished_nums = []

        for num in nums:
            if num == val:
                k+=1
            else:
                refurbished_nums.append(num)
        
        
        nums[:] = refurbished_nums + ([-1]*k)
        return len(refurbished_nums)
            