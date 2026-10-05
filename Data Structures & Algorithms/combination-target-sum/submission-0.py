class Solution:

    



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # given an array of distinct integers nums
        # target integer target

        # return a list of all unique combinations of nums, 
        # where the chosen numbers sum to target.

        # the same number may be chosen from nums an unlimited amount of times.
        # two combinations are teh same if the frequency of each chosen number is the 
        # same, otherwise they are different.

        # return the combinations in any order
        # and the order of numbers in each entry can be in any order.

        res = []

        def dfs(i, currentList, total):
            if total > target or (i >= len(nums)):
                return
            
            if total == target:
                res.append(currentList.copy())
                return

            # Include i
            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])
            
            # Exclude i, undo include by .pop()
            currentList.pop()
            dfs(i + 1, currentList, total)
            
        dfs(0, [], 0)
        
        return res

        