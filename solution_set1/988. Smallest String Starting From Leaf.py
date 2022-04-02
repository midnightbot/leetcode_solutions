##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        ## just make all strings, rev, sort, return
        
        ans = set()
        
        def expand(root,thisans):
            
            if root.left or root.right:
                if root.left:
                    expand(root.left, thisans + chr(ord('a') + root.val))
                    
                if root.right:
                    expand(root.right, thisans + chr(ord('a') + root.val))
                    
            else:
                res = thisans + chr(ord('a') + root.val)
                
                ans.add(res[::-1])
        
        expand(root,"")
        ans = list(ans)
        ans = sorted(ans)
        return ans[0]
