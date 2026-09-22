class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False;

        map1, map2 = {}, {}

        for char1,char2 in zip(s,t):

            if char1 in map1:
                map1[char1] += 1
            else:
                map1[char1] = 1
            
            if char2 in map2:
                map2[char2] += 1
            else:
                map2[char2] = 1
        
        print(map1,map2)
            
        return map1 == map2
        