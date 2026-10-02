"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # O (nlogn) Time Complexity, through .sort (...)
        # O (n) Memory Complexity, as .sort ( ... ) uses O(n) auxiliary space 

        intervals.sort(key = lambda k: k.start) 

        for i in range (len(intervals) - 1):

            nextMeeting = intervals[i+1]
            currMeeting = intervals[i]

            if currMeeting.end > nextMeeting.start:
                return False

        return True

