class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        low = prices[0] 

        for i in range(1,len(prices)):
            low = min(low,prices[i])
            res = max(prices[i]-low, res)
            print(low,res)
        
        return res



        