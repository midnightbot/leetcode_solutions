# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        ans = [0]
        
        @lru_cache(None)
        def expand(root):
            if not root:
                return 0
            
            left_len = expand(root.left)
            right_len = expand(root.right)
            
            l = r = 0
            
            if root.left and root.left.val == root.val:
                l+=1 + left_len
                
            if root.right and root.right.val == root.val:
                r+=1 + right_len
                
            ans[0] = max(ans[0],l+r)
            return max(l,r)
            
        expand(root)
        return ans[0]
        
