# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        root = head
        
        ans = []
        
        while head.next:
            ans.append(head.val)
            head = head.next
         
        ans.append(head.val)
        finals = root
        if len(ans) - n == 0:
            return root.next
        
        k = ans[len(ans)-n]
        prev = root
        
        
        
        c = 0
        while c<len(ans)-n:
            c+=1
            prev = root
            root = root.next
        #print(prev,root)
        prev.next = root.next
        return finals
            
        
