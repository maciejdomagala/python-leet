"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)[2:]
        temp = n[0]
        for a in n[1:]:
            if a == temp:
                return False
            
            else:
                temp = a
                
                
        return True
            