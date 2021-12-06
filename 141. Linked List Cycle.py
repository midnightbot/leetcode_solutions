##Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = []
        
        while head:
            if head not in visited:
                visited.append(head)
            
                head = head.next
                
            else:
                return True
            
            
        return False
        
