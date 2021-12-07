# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head!=None and head.next!=None:
            
            temp1 = head
            temp2 = head.next
            
            temp1.next = self.swapPairs(temp2.next)
            temp2.next = temp1
            
            return temp2
        
        return head
        
