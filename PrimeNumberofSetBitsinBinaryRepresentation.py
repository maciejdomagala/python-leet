"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
"""


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        for num in range(L, R+1):
            
            h = bin(num)[2:].count('1')
            if self.is_prime(h):
                ans += 1
    
        return ans 
    
    def is_prime(self, a):
        if a == 1:
            return False
        return all(a % i for i in xrange(2, a))
                
        
        
        
        