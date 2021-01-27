"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
 Find the two elements that appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e = 0
        for a in nums:
            e ^= a
            
        #finding last set bit in the number
        e &= -e
        
        #now 'e' is the number with only one '1' bit in the
        #position of last set to '1' bit in previous e
        
        print(e)
        
        a0, a1 = 0,0
        for a in nums:
            if a & e != e:
                a1 ^= a
            else:
                a0 ^= a
                
        return [a0,a1]
            