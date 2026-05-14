/**
 * Definition of Interval:
 * class Interval(var start: Int, var end: Int) {}
 */

class Solution {
    fun canAttendMeetings(intervals: List<Interval>): Boolean {
        val sortedIntervals = intervals.sortedBy { it.start }

        for(i in 0 until sortedIntervals.lastIndex) {
            val current = sortedIntervals[i]
            val next = sortedIntervals[i + 1]

            if (current.end > next.start) return false
        }
        return true
    }
}
