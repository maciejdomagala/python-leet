"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = ['']
        
        for ch in S:
            if ch.isalpha():
                ans = [i+j for i in ans for j in [ch.lower(), ch.upper()]]
            else:
                ans = [i+ch for i in ans]
                
        return ans
            