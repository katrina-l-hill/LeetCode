# 253. Meeting Rooms II

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106


import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        size = len(intervals)
        if size <= 1:
            return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0] >= heap[0]:
                heapq.heappushpop(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)
