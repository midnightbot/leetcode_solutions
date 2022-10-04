##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ##left,right,root so basically children then parent
        result = []
        
        def expand(root):
            if root:
                if root.children!=None:
                    for y in root.children:
                        expand(y)
                        
                result.append(root.val)
            
            
        expand(root)
        return result
        
