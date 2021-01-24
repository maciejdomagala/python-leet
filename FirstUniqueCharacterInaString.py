"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for a in s:
            if s.count(a) == 1:
                return s.index(a)
        return -1
        