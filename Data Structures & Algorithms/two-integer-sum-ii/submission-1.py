class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            twoSum = numbers[l] + numbers[r]

            if twoSum < target:
                #increment left pointer to increase our total
                l += 1
            elif twoSum > target:
                #decrement right pointer to decrease our total
                r -= 1
            else:
                #return solution
                return [l+1,r+1]



        