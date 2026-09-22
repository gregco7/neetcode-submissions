class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Given an array of the appearing ints, sorted in ascending order with most frequent at the top
        #return a list comprehension
        #return [ for i in range( len(list)-1, len(list)-(k+1),-1 ) ]

        count = {}
        freq = [[] for i in range(len(nums) + 1)] # a list of lists, nums+1 length long
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        # 0:2 , 5:3, 6:2
        for n,c in count.items():
            freq[c].append(n) 
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result



        