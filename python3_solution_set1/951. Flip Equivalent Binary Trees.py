##ss
##simple recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        if root1 == root2:
            return True
        
        if root1 is None or root2 is None or root1.val!=root2.val:
            return False
        
        
        return (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right) or self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))
        
