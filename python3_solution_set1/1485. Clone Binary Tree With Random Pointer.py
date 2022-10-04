##ss
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        self.dicts = {}
        
        def maketree(root):
            
            if root is None:
                return root
           
            if root in self.dicts:
                return self.dicts[root]
            
            newnode = NodeCopy(root.val)
            
            self.dicts[root] = newnode
            self.dicts[root].left = maketree(root.left)
            self.dicts[root].right = maketree(root.right)
            self.dicts[root].random = maketree(root.random)
            
            
            return newnode
        
        
        return maketree(root)
