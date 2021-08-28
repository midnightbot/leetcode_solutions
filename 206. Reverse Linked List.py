# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = []
        
        while head:
            ans.append(head.val)
            head = head.next
            
        #print(ans)
        ans = ans[::-1]
        
        final = temp = ListNode()
        
        for x in ans:
            temp.next = ListNode(x)
            temp = temp.next
            
        return final.next
        
