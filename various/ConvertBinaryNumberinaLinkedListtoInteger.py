"""
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next
            
        return int(''.join([str(a) for a in vals]),2)
        
        