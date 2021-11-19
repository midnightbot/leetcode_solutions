# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root = head
        lens = 0
        while head.next:
            lens+=1
            head = head.next
            
        lens+=1
        if lens%2!=0:
            mid = int((lens-1)/2 + 1)
            
        else:
            mid = int((lens/2) + 1)
            
        c = 0
        finals = root
        prev = root
        while c<mid-1:
            c+=1
            root = root.next
            
        return root
