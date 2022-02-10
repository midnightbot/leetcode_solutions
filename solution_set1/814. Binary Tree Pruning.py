##ss
##simple recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def check(node):
            
            if node is None:
                return False
            
            left = check(node.left)
            right = check(node.right)
            
            if left == False:
                node.left = None
                
            if right == False:
                node.right = None
                
            return node.val==1 or left or right
        
        ans = check(root)
        if ans == True:
            return root
        else:
            return None
        
        
