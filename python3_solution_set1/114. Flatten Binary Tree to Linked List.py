##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def preorder(root):
            
            if root is None:
                return None
            
            if root.left is None and root.right is None:
                return root
            
            l = preorder(root.left)
            r = preorder(root.right)
            
            
            if l:
                l.right = root.right
                root.right = root.left
                root.left = None
                
            return r if r else l
        
        return preorder(root)
