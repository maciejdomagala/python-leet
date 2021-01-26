"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.


"""

#VERY PYTHONIC WAY

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if set(digits) == set([0]):
            digits[-1] = 1
            return digits
        return [int(b) for b in str((int(''.join([str(a) for a in digits])) + 1))]