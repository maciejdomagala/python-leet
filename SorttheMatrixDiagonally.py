"""
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
"""

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        
        ind = []
        val = []
        
        for i in range(m):
            j = 0
            while i < m and j < n:
                ind.append([i, j])
                val.append(mat[i][j])
                i += 1
                j += 1
                
            val = sorted(val)
            
            for k, a in enumerate(ind):
                mat[a[0]][a[1]] = val[k]
                
            val = []
            ind = []
            
        for j in range(1, n):
            i = 0
            while i < m and j < n:
                ind.append([i,j])
                val.append(mat[i][j])
                i += 1
                j += 1
                
            val = sorted(val)
            
            for k, a in enumerate(ind):
                mat[a[0]][a[1]] = val[k]
                
            val = []
            ind = []
            
        return mat
                
        