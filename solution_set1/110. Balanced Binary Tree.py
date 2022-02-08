# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #print(root,'\n')
        if root is None:
            return True
        
        return (abs(self.check(root.left) - self.check(root.right)) <=1  and self.isBalanced(root.left) and  self.isBalanced(root.right))
        
    def check(self,root):
        if root is None:
            return -1
        return 1 + max(self.check(root.left),self.check(root.right))
        
