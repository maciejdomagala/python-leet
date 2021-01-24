"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different 
digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous
 section all of the same character. Then for each group, say the number of characters, then say the character. 
 To convert the saying into a digit string, replace the counts with a number and concatenate every saying.


Given a positive integer n, return the nth term of the count-and-say sequence.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        s = self.converter("1")
        
        for i in range(n-2):
            s = self.converter(s)
            
        return s
        
    def converter(self, string):
        
        if string == '1':
            return "11"
        
        s = string[0]
        k = 1
        ans = []
        
        for i in range(1, len(string)):
            if string[i] == s:
                k += 1
            else:
                ans += [str(k),s]
                s = string[i]
                k = 1
                
        ans += [str(k),s]
                
        return ''.join(ans)
            