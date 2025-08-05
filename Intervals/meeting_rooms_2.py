class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: list[Interval]) -> int:
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])

        start_ptr = 0
        end_ptr = 0
        room_count = 0
        max_rooms = 0

        while start_ptr < len(start_times):
            start = start_times[start_ptr]
            end = end_times[end_ptr]

            if start < end:
                room_count += 1
                start_ptr += 1
                max_rooms = max(max_rooms, room_count)
            else:
                room_count -= 1
                end_ptr += 1
            
        
        return max_rooms