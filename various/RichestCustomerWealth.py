"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount
of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
"""

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxx = 0
        for a in accounts:
            if sum(a) > maxx:
                maxx = sum(a)
                
        return maxx
        