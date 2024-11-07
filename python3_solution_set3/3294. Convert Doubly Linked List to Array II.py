"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        
        node_l = copy.deepcopy(node)
        arr_l = []
        arr_r = []

        while node is not None:
            arr_r.append(node.val)
            node = node.next

        while node_l is not None:
            arr_l.append(node_l.val)
            node_l = node_l.prev

        return arr_l[::-1] + arr_r[1:]
        
