##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        self.dicts = {}
        
        def makell(head):
            
            if head is None:
                return None
            
            if head in self.dicts:
                return self.dicts[head]
            
            
            newnode = Node(head.val,None,None)
            self.dicts[head] = newnode
            newnode.next = makell(head.next)
            newnode.random = makell(head.random)
            
            return newnode
        
        return makell(head)
        
