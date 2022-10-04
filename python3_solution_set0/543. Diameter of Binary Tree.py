# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = []
        self.expand(root,ans)
        return max(ans)
        
    def expand(self,root,ans):
        if root == None:
            return 0
        
        l = self.expand(root.left,ans)
        r = self.expand(root.right,ans)
        
        ans.append(l+r)
        #ans = max(ans, l+r)
        #print(ans)
        
        return max(l,r) + 1
        
        
        
        
        
