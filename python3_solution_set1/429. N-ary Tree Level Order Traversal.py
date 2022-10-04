##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root is None:
            return root
        ans = []
        
        q = [root]
        
        while q:
            temp = []
            for x in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                
                if node.children:
                    for z in node.children:
                        q.append(z)
                    
            ans.append(temp)
            
        return ans
        
