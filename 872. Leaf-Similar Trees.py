##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        ans1 = []
        
        ans2 = []
        visited = []
        self.dfs(visited,root1,ans1)
        self.dfs([],root2,ans2)
        
        return ans1==ans2
    def dfs(self,visited,root,ans):
        if root not in visited:
            visited.append(root)
            
            if root.left:
                self.dfs(visited,root.left,ans)
            if root.right:
                self.dfs(visited,root.right,ans)
                
            if root.left == None and root.right == None:
                ans.append(root.val)
            
