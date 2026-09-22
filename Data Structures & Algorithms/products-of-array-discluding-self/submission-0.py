class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums: return [];

        zeroCheck = False
        bigNum = 1

        outp = [0] * len(nums) #placeholder

        for num in nums:
            if num == 0: 
                if zeroCheck:
                    return [0] * len(nums)
                else:
                    zeroCheck = True
            else:
                bigNum *= num
        
        

        if zeroCheck:
            for index,num in enumerate(nums):
                if num != 0:
                    outp[index] = 0
                else:
                    outp[index] = int(bigNum)
        else:
            for index,num in enumerate(nums):
                outp[index] = int(bigNum/num)

        print(bigNum)
        return outp


        