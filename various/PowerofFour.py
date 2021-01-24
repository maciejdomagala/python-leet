"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        f = False
        i = 1
        while n:
            c = (n & 1)
            
            if c == 1:
                if i % 2 == 0:
                    return False
                if f == True:
                    return False
                else:
                    f = True
                    
            n = n >> 1
            i += 1
            
        return f
            
            
                
            