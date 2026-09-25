class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #edge case where only one price, just don't buy. U can't sell and make profit
        if len(prices) <= 1: return 0;

        res = 0
        low = prices[0] # 5, 1

        for i in range(1,len(prices)):
            low = min(low,prices[i])
            res = max(prices[i]-low, res)
            print(low,res)
        
        return res



        