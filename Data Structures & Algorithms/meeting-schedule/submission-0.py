"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # given an array of meeting time interval objects (start_1, end_1) ~ list of tuples
        # determine if a person could add all meetings to their schedule without any conflicts.
        # the intervals may be provided in any order
        # (0,8) -> (8,10) is not considered a conflict
        # [ ... ) inclusive and exclusive.

        # to clarify, two meetings are going to explicitly conflict if we are returning false so ... 
        # what makes two meetings conflict 

        # (0,8) ... (8,10) good 8 - 8 = 0 ... ? good

        # (5,10) ... (15,20) good 15 - 10 = 5 ... good?
        # (0,30) ... (5,10) bad 5 - 30 = -25 ... bad?

        # do meetings conflict explicitly when 2[0] - 1[1] < 0 ?
        # I mean, this is true when 2 is ahead of 1 meaning 2[0] > 1[0] but not always applicable its not ordered
        # in any way.

        # you can sort in O(logn) btw
        # and then compare in O(n) seperately?
        # should sizzle down to O(n) complexity and no extra memory

        intervals = sorted((tup for tup in intervals), key = lambda k: k.start) # should sort by ascending start dates

        for i in range (len(intervals) - 1):

            nextMeeting = intervals[i+1]
            currMeeting = intervals[i]

            if (nextMeeting.start - currMeeting.end) < 0:
                return False

        return True

