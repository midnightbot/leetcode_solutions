# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}

        while head:
            freq[head.val] = freq.get(head.val,0) + 1
            head = head.next

        freq = [freq[x] for x in freq]

        def make_ll(indx):
            if indx == len(freq):
                return None
            new_node = ListNode()
            new_node.val = freq[indx]
            new_node.next = make_ll(indx+1)
        
            return new_node

        return make_ll(0)
