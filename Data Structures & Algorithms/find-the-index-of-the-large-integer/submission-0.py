# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        size = reader.length()
        left = 0
        right = size - 1

        while left < right:
            length = right - left + 1
            half = length // 2
            result = reader.compareSub(left, left + half - 1, left + half, left + 2 * half - 1)
            if result == 0:
                return right
            elif result == 1:
                right = left + half - 1
            else:
                left = left + half
        return left