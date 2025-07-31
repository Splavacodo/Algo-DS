class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            upper_bound = merged[-1][1]

            if start <= upper_bound:
                merged[-1][1] = max(end, upper_bound)
            else:
                merged.append([start, end])
        
        return merged