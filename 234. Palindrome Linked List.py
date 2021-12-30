##ss

##Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        comp = []
        
        while head:
            comp.append(head.val)
            head = head.next
            
        return comp == comp[::-1]
        
        
## Solution 2
