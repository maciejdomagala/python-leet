"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
"""

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        """
        idea: using a staircase to descend from top right to botom left, when seeing -1 - moving 
        to the left, if +, to the right and check again. add all positions to the index
        """
        
        #i - rows (m)
        #j - colums (n)
        
        j = n - 1
        i = 0
        ans = 0
        
        while i < m and j > -1:
            if grid[i][j] < 0:
                ans += m - i
                j -= 1
            else:
                i += 1
                
        return ans
                