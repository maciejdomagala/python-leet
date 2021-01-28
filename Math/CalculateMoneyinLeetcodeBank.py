"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        week = n // 7
        mod = n % 7

        a = ((56 + 7*(week-1))*week)/2
        b = (2*week + mod + 1)*(mod)/2
        
        return int(a+b)