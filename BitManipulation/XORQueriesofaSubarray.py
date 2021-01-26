"""
Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], 
for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ).
Return an array containing the result for the given queries.
"""

class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        for i in range(len(arr)-1):
            arr[i+1] ^= arr[i]
        
        return [arr[j] ^ arr[i - 1] if i else arr[j] for i,j in queries]