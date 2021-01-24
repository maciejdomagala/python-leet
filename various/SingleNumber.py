"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e = 0
        for a in nums:
            e ^= a
            
        return e

"""
This is solution based on bit manipulation. We are using XOR to 'reduce' the bits in base2 representation when
we are seeing a given number twice. Only bits from single number will be left.
"""