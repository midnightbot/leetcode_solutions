# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        parents = root.val
        
        ps = p.val
        qs = q.val
        
        if ps>parents and qs > parents: ##both p and q on right side hence lca can be on the next level
            return self.lowestCommonAncestor(root.right,p,q)
        
        elif ps<parents and qs<parents: ##both p and q on left side hence lca can be on the next level
            return self.lowestCommonAncestor(root.left,p,q)
        
        else: ##p and q on different branches hence this is their lca
            return root
            

        
