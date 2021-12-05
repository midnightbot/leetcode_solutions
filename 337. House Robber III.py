# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        ans = self.robbing(root,memo)
        return ans
        
        
    def robbing(self,root,memo):
        
        if root == None:
            return 0
        
        if root in memo.keys():
            return memo[root]
        
        ans = 0
        
        if root.left:
            ans+= self.robbing(root.left.left,memo) + self.robbing(root.left.right,memo)
            
        if root.right:
            ans+=self.robbing(root.right.left,memo) + self.robbing(root.right.right,memo)
            
        
        memo[root] = max(root.val + ans, self.robbing(root.left,memo)+self.robbing(root.right,memo))
        return memo[root]
        
