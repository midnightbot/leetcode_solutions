##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.ans = 0
        
        def transform(root):
            if root is None:
                return None
            
            else:
                transform(root.right)
                self.ans+=root.val
                root.val = self.ans
                transform(root.left)
                return root
            
        return transform(root)
