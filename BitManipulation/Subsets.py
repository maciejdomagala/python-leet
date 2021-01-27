"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for num in range(2**len(nums)):
            i = 0
            ind = []
            while num:
                if num & 1:
                    ind.append(i)
                
                num = num >> 1
                i += 1
                
            ans.append([nums[i] for i in ind])
            
        return ans
            