class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs (i,currList,currSum):
            if i >= len(nums) or currSum > target:
                return
            
            if currSum == target:
                res.append(currList.copy())
                return
            
            # stay at i 
            currList.append(nums[i])
            dfs(i,currList,currSum + nums[i])

            # skip and go to i + 1
            currList.pop()
            dfs(i+1,currList,currSum)

        dfs(0,[],0)

        return res