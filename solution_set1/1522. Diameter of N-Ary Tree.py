##ss
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        self.anss = 0
        
        def expand(root):
            
            if root is None:
                return root
            
            if root.children:
                ans = []
                for z in root.children:
                    ans.append(1+expand(z))

                ans = sorted(ans)
                
                if len(ans) >= 2:##if root has two or more children, answer is sum of length of the two roots farthest from it
                    self.anss = max(self.anss, ans[-1] + ans[-2])
                    
                else:##if only one child, ans is farthest node from it
                    self.anss = max(self.anss, ans[-1])
                    
                return max(ans)##used for calculation of answer for upper parent node
            else:
                return 0
        expand(root)
        return self.anss
