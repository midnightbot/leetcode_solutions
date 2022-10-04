# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = []
        while head:
            
            temp.append(head.val)
            head = head.next
            
        #temp.append(head.val)
        temp = sorted(temp)
        
        finals = ans = ListNode()
        for x in temp:
            #print(ListNode(x))
            ans.next = ListNode(x)
            ans = ans.next
            print(ans)
            
        return finals.next
            
 
            
            
            
            
            
        
