class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        largestSequence = 0

        for num in nums:
            #if theres a left neighbor, I don't care
            if (num-1) in numSet: continue;
            #no left neighbor: this is the start of a sequence.

            tempSequence = 1
            while (num+1) in numSet:
                tempSequence += 1
                num+=1
            largestSequence = max(tempSequence,largestSequence)
        
        return largestSequence












        