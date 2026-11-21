class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        // given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
        // you may choose a single day to buy one NeetCoin and choose a different day in the
        // future to sell it.
        // return the maximum profit you can achieve, you may choose to not make any transactions
        // in which case the profit would be 0
        // example prices = [10,1,5,6,7,1]
        // output: 6

        // Approach: Sliding Window
        // Keep a left and right pointer, where left < right, left and right < length of prices
        // then iterate through the array, updating the pointers, choosing to either
        // increment the left or right pointer at each iteration, whichever would result in a stronger profit.
        //   if l >= r - 1, r must be incremented to avoid collision, but if
        //    if l > r, l increments
        //    if r >= l, r increments

        let profit = 0;
        let l = 0;
        let r = 1;

        if (prices.length === 0) {
            return profit;
        }

        while (r < prices.length) {
            profit = Math.max(profit,(prices[r]-prices[l]));
            if (prices[l] > prices[r]) {
                l = r;
            } else {
                r++;
            }            
        }
        return profit;
    }
}
