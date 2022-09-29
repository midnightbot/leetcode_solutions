# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ## root.left => newroot
        ## root => newroot.right
        ## root.right => newroot.left
        
        if root == None or (root.left == None and root.right == None):
            return root
        
        new_node = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        
        root.left = None
        root.right = None
        
        return new_node
        
                
                
                
        
        
