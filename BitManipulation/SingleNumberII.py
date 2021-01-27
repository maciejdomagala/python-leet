"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        idea:
        keep two 'sets', one keeps the track when number
        appears first time,
        second when number appears second time.
        """
        
        ones, twos = 0,0
        
        for a in nums:
            ones = (ones ^ a) & ~twos
            twos = (twos ^ a) & ~ones
            
        return ones
            