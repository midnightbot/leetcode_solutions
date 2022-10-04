# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        oddnode = ListNode(0)
        evennode = ListNode(0)
        
        oddh = oddnode
        evenh = evennode
        
        odd = True
        
        while head:
            if odd:
                oddnode.next = head
                oddnode = oddnode.next
                
            else:
                evennode.next = head
                evennode = evennode.next
                
            odd = not (odd)
            head = head.next
            
        evennode.next=None
        oddnode.next = evenh.next
        return oddh.next
