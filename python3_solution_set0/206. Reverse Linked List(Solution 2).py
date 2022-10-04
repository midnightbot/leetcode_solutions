# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        ans = ListNode()
        ans.val = head.val
        ans.next = None
        prev_ans = ans
        while head.next!=None:
            head = head.next
            
            ans = ListNode()
            ans.val = head.val
            ans.next = prev_ans
            prev_ans = ans
            
        return ans
            
            
        
