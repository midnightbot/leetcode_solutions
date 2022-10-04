##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = []
        
        temp = 0
        while head:
            if head.val == 0:
                ans.append(temp)
                temp = 0
                
            else:
                temp+=head.val
                
            head = head.next
        
        return self.makelist(ans,1)
    def makelist(self,ans,p):
        if p == len(ans):
            return None
        if p < len(ans):
            root = ListNode()
            root.val = ans[p]
            root.next = self.makelist(ans,p+1)
            
            return root
            
        
