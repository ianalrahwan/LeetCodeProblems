# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            current = start + ((end - start) // 2)
            if isBadVersion(current):
                end = current
            else:
                start = current + 1
        return start

            