class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if intervals[0][0] >= newInterval[0]:
            if intervals[0][0] > newInterval[1]:
                return [newInterval] + intervals
            else:
                intervals[0][0] = min(intervals[0][0], newInterval[0])
                intervals[0][1] = max(intervals[0][1], newInterval[1])
                hasInserted = True

        skipped = 0
        swap = None
        hasInserted = False
        for i in range(len(intervals)):
            if not hasInserted:
                print("F", intervals[i])
                print("FN", newInterval)
                if intervals[i][1] < newInterval[0]:
                    continue
                elif intervals[i][1] == newInterval[0] or intervals[i][0] <= newInterval[0]:
                    intervals[i][1] = max(newInterval[1], intervals[i][1])
                    hasInserted = True
                else:
                    swap = intervals[i]
                    intervals[i] = newInterval
                    hasInserted = True
            elif swap:
                tmp = intervals[i]
                intervals[i] = swap
                tmp = swap
            else:
                # if i + skipped >= len(intervals):
                #     break

                if intervals[i][0] <= intervals[i-1-skipped][1]:
                    # print("skip", intervals[i-1-skipped], intervals[i])
                    intervals[i-1-skipped][1] = max(intervals[i][1], intervals[i-1-skipped][1])
                    # print("after", intervals[i-1-skipped])
                    skipped += 1
                elif skipped:
                    # print("skip2", intervals[i-1-skipped], intervals[i])
                    intervals[i-skipped] = intervals[i]
                else:
                    break

        if not hasInserted:
            intervals.append(newInterval)
        elif swap:
            intervals.append(swap)
        else:
            while skipped > 0:
                intervals.pop()
                skipped -= 1

        return intervals
