##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        
        @lru_cache(None)
        def expand(root):
            if not root:
                return 0
            
            l = expand(root.left)
            r = expand(root.right)
    
            self.ans = max(self.ans,root.val, root.val + l, root.val + r, l+ r + root.val)
            return max(root.val, root.val + l, root.val + r)
            
        expand(root)
        return self.ans
        
