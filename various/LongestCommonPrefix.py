"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = 0
        it = zip(*strs)
        
        for a in it:
            if len(set(a)) == 1:
                ans += 1
            else:
                break
                
        return strs[0][:ans] if ans > 0 else ""