##Same as question 141
##Step 1 : Using tortoise and hare technique find if cycle exists
##Step 2 : If cycle is present find intersection point
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        
        if head == None:
            return None
        pt2 = head
        pt = self.findcycle(head)
        if pt == None:
            return None
        #pt2 = head
        while pt!=pt2:
            pt2 = pt2.next
            pt = pt.next
            
        return pt2
        
        
    def findcycle(self,head):
        if head == None or head.next == None:
            return None
        
        tortoise = head
        hare = head
        
        while hare!=None and hare.next!=None:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return tortoise
            
            
        return None
        
