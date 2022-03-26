##ss
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        nodes = []
        
        while head:
            nodes.append(head.val)
            head = head.next
            
        nodes[k-1],nodes[-k] = nodes[-k],nodes[k-1]
        
        
        def make(pos):
            
            if pos == len(nodes) - 1:
                return ListNode(nodes[pos])
            
            else:
                node = ListNode()
                node.val = nodes[pos]
                node.next = make(pos+1)
                
                return node
            
            
        return make(0)
