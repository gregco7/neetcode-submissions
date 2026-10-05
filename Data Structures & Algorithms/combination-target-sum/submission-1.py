class Solution:

    



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, currList, total):

            if i >= len(nums) or total > target:
                return
            
            if total == target:
                res.append(currList.copy())
                return
            
            #Include i
            currList.append(nums[i])
            dfs(i, currList, total + nums[i])

            #Exclude i
            currList.pop()
            dfs(i+1, currList, total)

        dfs(0, [], 0)
        return res
        
        

        