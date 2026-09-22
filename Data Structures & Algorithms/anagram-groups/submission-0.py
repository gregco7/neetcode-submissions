class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ourMap = defaultdict(list)

        for string in strs:
            count = [0] * 26 # a through z
            for character in string:
                count[ord(character) - ord("a")] += 1
            # [0,2,0,4,0,0, ... ] but cannot but a key so must become a tuple
            ourMap[tuple(count)].append(string) # the key for ourmap must be converted to an immutable tuple, can't use maps/list as keys
        
        return list(ourMap.values())

            
        



        