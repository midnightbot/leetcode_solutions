# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        ans = self.result = TreeNode(None, None, None)
        self.dfs(original,cloned,target)
        return ans.right
    def dfs(self, original : TreeNode, cloned: TreeNode, target:TreeNode):
        
        if original == None:
            return
        
        if original == target:
            self.result.right = cloned
            return
        
        self.dfs(original.left, cloned.left,target)
        self.dfs(original.right,cloned.right,target)
            
    
        
