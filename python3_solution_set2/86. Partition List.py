# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a = []
        b = []
        
        while head:
            if head.val < x:
                a.append(head.val)
                
            else:
                b.append(head.val)
            head = head.next
            
        ans = a + b
        
        def make_ll(indx):
            if indx == len(ans):
                return None
            else:
                new_node = ListNode()
                new_node.val = ans[indx]
                new_node.next = make_ll(indx+1)
                return new_node
        return make_ll(0)
