"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(l)):
            current_el = l[i - 1]
            next_el = l[i]

            if current_el.end > next_el.start:
                return False

        return True