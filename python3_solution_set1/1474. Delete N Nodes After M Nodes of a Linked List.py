##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        result = head
        
        count = 1
        while head:
            
            if count % m == 0:
                
                thisnode = head
                #print(thisnode.val)
                ##upd thisnode.next
                dels = 0
                while dels!=n+1 and head:
                    #count+=1
                    dels+=1
                    prev = head
                    head = head.next
                    
                if dels == n+1:
                    thisnode.next = prev.next
                    prev.next = None
                    
                else:
                    thisnode.next = None
                    
            
            else:
                head = head.next
                
            count+=1
        
        
        
        return result
        
