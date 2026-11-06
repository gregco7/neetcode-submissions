class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        given two strings s1 and s2
        return true if s2 contains a permutation of s1 or false otherwise
        """

        len1, len2 = len(s1), len(s2)
        if len2 < len1:
            return False
        
        l,r = 0,0

        charMap = {} # char : freq

        for c in s1:
            charMap[c] = charMap.get(c,0) + 1

        unfulfilled = len(charMap)
        
        while r < len2:
            leftC = s2[l]
            rightC = s2[r]

             # increment pointers
            if r - l >= len1:
                if leftC in charMap:
                    if charMap[leftC] == -1:
                        unfulfilled -= 1
                    elif charMap[leftC] == 0:
                        unfulfilled += 1
                    charMap[leftC] += 1
                l += 1

            # append running window
            if rightC in charMap:
                if charMap[rightC] == 0:
                    unfulfilled += 1
                elif charMap[rightC] == 1:
                    unfulfilled -= 1

                charMap[rightC] -= 1
            
            r += 1
            if unfulfilled == 0:
                return True

        return False
