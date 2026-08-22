class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        refurbishedList = []

        for index, num in enumerate(arr):
            if index == len(arr) - 1:
                refurbishedList.append(-1)
            else:
                num = max(arr[index+1:])
                refurbishedList.append(num)
        
        return refurbishedList
            

        