class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newStart = newInterval[0]
        newEnd = newInterval[1]

        for i in range (len(intervals)):
            intStart,intEnd = intervals[i][0],intervals[i][1]
            # Check Overlap Ascending & Descending
            if ((intStart <= newStart) and (intEnd >= newStart)) or ((intStart >= newStart) and (newEnd >= intStart)):
                # Overlap, begin merge chain
                startMerge, endMerge = i,i

                while (endMerge < len(intervals) - 1) and (newEnd >= intervals[endMerge+1][0]):
                    endMerge += 1

                end = [[ min(intervals[startMerge][0],newInterval[0]) , max( intervals[endMerge][1],newInterval[1] ) ]]
                if endMerge < len(intervals) - 1:
                    end += intervals[endMerge+1:]
                
                return intervals[0:startMerge] + end
            
            # We have began descending but no overlap, so we merge and end early.
            if (intStart > newStart):
                # No Overlap
                return intervals[0:i] + [newInterval] + intervals[i:]
        
        return intervals + [newInterval]
