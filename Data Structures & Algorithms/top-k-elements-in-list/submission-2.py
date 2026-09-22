class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Given an array of the appearing ints, sorted in ascending order with most frequent at the top
        #return a list comprehension
        #return [ for i in range( len(list)-1, len(list)-(k+1),-1 ) ]

        freqMap = defaultdict(int) # Key:Value | number (int) :appearanceCount (int)

        for num in nums:
            freqMap[num] += 1

        #print(freqMap)
        
        ourList = dict(sorted(freqMap.items(), key=lambda item: item[1])) # sort by ascending frequency
        #print(ourList)
        ourList = list(ourList.keys())

        return [ourList[i] for i in range (len(ourList)-1, len(ourList)-(k+1),-1)]




        