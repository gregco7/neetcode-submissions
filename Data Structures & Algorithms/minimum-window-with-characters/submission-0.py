class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        charmap, window = {}, {}

        for c in t:
            charmap[c] = charmap.get(c,0) + 1

        res,resLen = [-1,-1], float("infinity")
        l = 0

        need = len(charmap)
        have = 0

        for r in range(len(s)):
            c = s[r]

            window[c] = window.get(c,0) + 1

            if c in charmap and window[c] == charmap[c]:
                have += 1
            
            while need == have:
                windowLen = r - l + 1
                if windowLen < resLen:
                    res = [l,r]
                    resLen = windowLen
                
                # pop left until window no longer valid
                window[s[l]] -= 1

                if s[l] in charmap and window[s[l]] < charmap[s[l]]:
                    have -= 1

                l += 1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

