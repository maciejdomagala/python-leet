"""
Given an integer array arr. 
You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and 
in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.
"""

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for a in arr:
            ans.append((a, self.countBits(a)))
            
        return [a[0] for a in sorted(ans, key = lambda x: (x[1], x[0]))]
            
            
            
    def countBits(self, n):
        
        count = 0
        while n:
            count += (n & 1)
            n = n >> 1
        
        return count
        
        