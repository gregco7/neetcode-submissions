class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map1, map2 = {}, {}

        for char1 in s:

            if char1 in map1:
                map1[char1] += 1
            else:
                map1[char1] = 1
        
        for char2 in t:
            if char2 in map2:
                map2[char2] += 1
            else:
                map2[char2] = 1
        
        print(map1,map2)
            
        return map1 == map2
        