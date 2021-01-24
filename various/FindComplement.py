"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_b = bin(num)[2:]
        ans = ''.join(['0' if a == '1' else '1' for a in num_b])
        return int(ans, 2)