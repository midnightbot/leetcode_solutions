##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        c = {}
        
        while head:
            c[head.val] = c.get(head.val,0) + 1
            head = head.next
            
        use = [x for x in c if c[x] == 1]
        
        
        def makelist(pos):
            if pos == len(use) - 1:
                return ListNode(use[pos])
            
            else:
                node = ListNode()
                node.val = use[pos]
                node.next = makelist(pos+1)
                
                return node
        
        if len(use)!=0:
            return makelist(0)
        else:
            return None
        
