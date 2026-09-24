class Solution:

    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights) - 1
        maxVol = min(heights[l],heights[r]) * (r-l)

        #me move the pointer that has the smller height
        while l < r:
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1 #decrement right pointer when it pointer to something smaller, or its equal. It doesn't matter which pointer you alter when they point to equal values, as two large heights are needed to outpace the bottleneck.
            
            maxVol = max(maxVol,min(heights[l],heights[r]) * (r-l))

        return maxVol


        