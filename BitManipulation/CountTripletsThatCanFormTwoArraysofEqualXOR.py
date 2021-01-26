"""
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.
"""

class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        d = {0:[-1]}
        ans = 0
        i = 0
        
        while i < len(arr):
            res = arr[i]^res
            if res in d:
                temp = [i-x-1 for x in d[res]]
                d[res].append(i)
                ans += sum(temp)
            else:
                d[res] = [i]
                
            i += 1
                
        return ans