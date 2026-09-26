class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        charMap = {}
        res = 0
        l = 0

        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r],0) + 1

            #if window is invalid, bump l until its valid while decrementing values
            while (r-l+1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res






        
        