# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return head
        
        current = head.next
        previous = head
        
        while current!=None:
            if current.val == previous.val:
                previous.next = current.next
                current = current.next
                
            else:
                current = current.next
                previous = previous.next
                
        return head
                
        
            
        
