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
            
            
        
##Solution 3 (Classic hare and tortoise problem)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return False
        
        tortoise = head
        hare = head.next
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
            
        return False
        
        
            
        
        
