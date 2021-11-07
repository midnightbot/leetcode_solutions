# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root == None:
            return False
        
        targetSum-= root.val
        
        if root.left == None and root.right==None:
            if targetSum==0:
                return True
            else:
                return False
            
        return self.hasPathSum(root.left,targetSum)+ self.hasPathSum(root.right,targetSum)
        
        
        
        

        
        
