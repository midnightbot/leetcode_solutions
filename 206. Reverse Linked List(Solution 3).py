# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ##recursive implementation
        
        if head!=None and head.next!=None:
            
            temp = self.reverseList(head.next)
            print("hi",temp)
            head.next.next = head
            head.next = None
            
            return temp
        
        return head
        
