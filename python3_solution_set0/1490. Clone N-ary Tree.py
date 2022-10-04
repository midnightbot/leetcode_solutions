"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        if root == None:
            return None
        
        newnode = Node(root.val)
        for children in root.children:
            newnode.children.append(self.cloneTree(children))
            
        return newnode
