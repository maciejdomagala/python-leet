"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
         #two pointers approach
            
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1] 
            
            i += 1
            j -= 1
        
        return True