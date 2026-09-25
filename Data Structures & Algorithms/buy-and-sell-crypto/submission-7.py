class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Pointer Solutions

        l,r = 0,1
        res = 0 

        while r < len(prices):

            if prices[l] < prices[r]:
                #update max
                res = max(res,prices[r]-prices[l])
            else:
                #assign new min/left pointer
                l = r
            r += 1 #move the right pointer forward no matter what

        return res

        