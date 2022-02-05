##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root is None:
            return 0
        q = [(root,1)]
        
        ans = 0
        while q:
            node = q.pop()
            ans = max(ans,node[1])
            if node[0].children:
                for z in node[0].children:
                    if z!=None:
                        q.append((z,node[1]+1))
                        
        return ans
                        
                        
            
        
