##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def expand(root):
            if root is None:
                return 0
            
            a = expand(root.left)
            b = expand(root.right)
            self.ans+=abs(a) + abs(b)
            return root.val + a + b - 1
        
        
        expand(root)
        return self.ans
        
