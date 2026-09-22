class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums: return [];

        finalOutput = []
        prefixArr, postfixArr = [],[]

        for num1,num2 in zip(nums,reversed(nums)):
            #edge case, when the arrays are empty start them just with the first value
            if not (prefixArr or postfixArr):
                prefixArr.append(num1)
                postfixArr.append(num2)
                continue

            prefixArr.append(prefixArr[-1] * num1)
            postfixArr.append(postfixArr[-1] * num2)
        
        postfixArr.reverse()
        outp = []

        for index,num in enumerate(nums):
            #edge case, on first index [0] or the last index [-1]
            if index == 0: 
                outp.append(postfixArr[1])
                continue
            if index == (len(nums)-1): 
                outp.append(prefixArr[len(nums)-2])
                continue
    
            outp.append(prefixArr[index-1] * postfixArr[index+1])

        return outp


        



        