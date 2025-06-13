# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

## O(logn) time O(1) space
def isBadVersion(version):

    class Solution(object):
        def firstBadVersion(self, n):
            left = 1
            right = n
            while left < right:
                m = (left + right) // 2
                if not isBadVersion(m): ## if m is T
                    left = m + 1
                else:
                    right = m

            return left

## Perform conditional based binary search starting from 1 up to n
## check if m is T
## if it is move left over
## if not move right to m
## left pointer will end up being the first bad version