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
        
##Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False
        
        for x in range(pow(10,4)+1):
            if head.next!=None:
                head = head.next
                
            else:
                return False
            
        return True
            
            
        
        
