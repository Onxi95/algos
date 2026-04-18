"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
            sorted_intervals = sorted(intervals, key=lambda x: x.start)

            for i in range(len(sorted_intervals) - 1):
                current_end = sorted_intervals[i].end
                next_start = sorted_intervals[i + 1].start

                if current_end > next_start:
                    return False

            return True