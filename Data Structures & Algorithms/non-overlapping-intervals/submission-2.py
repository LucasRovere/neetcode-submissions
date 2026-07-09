class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        maxEnd = intervals[0][1]
        result = 0

        for interval in intervals[1:]:
            if interval[0] < maxEnd:
                result += 1
                maxEnd = min(maxEnd, interval[1])
            else:
                maxEnd = interval[1]

        return result