class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key = lambda interval : interval.start)
        prev = intervals[0].end

        for interval in intervals[1:]:
            start, end = interval.start, interval.end

            if start < prev:
                return False
            else:
                prev = end
        
        return True



