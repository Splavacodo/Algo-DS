class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_intervals = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if newInterval[1] < start:
                new_intervals.append(newInterval)
                return new_intervals + intervals[i:]
            elif newInterval[0] > end:
                new_intervals.append([start, end])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        new_intervals.append(newInterval)
        
        return new_intervals