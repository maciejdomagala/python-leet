"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.
"""

#important note:
# it is more efficient to just look at the number of 0s and 1s at given bit position and not calculating pair-wise hamming distance

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        ans = 0
        
        for i in range(32):
            a = 0
            b = 0
            for j in range(n):
                bit = 1 << i
                c = (nums[j] & bit) >> i
                if c == 0:
                    a += 1
                elif c == 1:
                    b += 1
                    
            ans += a * b
            
        return ans
        
        
        
        
        