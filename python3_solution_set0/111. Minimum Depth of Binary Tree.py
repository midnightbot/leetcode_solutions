##Solution 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        temp = []
        if root == None:
            return 0
        self.bfs(root,1,temp)
        return min(temp)
        
        
    def bfs(self,root,d,ans):
        
        if root.left:
            self.bfs(root.left,d+1,ans)
        if root.right:
            self.bfs(root.right,d+1,ans)
 
        if root.left == None and root.right == None:
            ans.append(d)
        

      
## Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = self.bfs(root)
        return ans
        
        
    def bfs(self,root):
        if root == None:
            return 0
        
        queue = []
        queue.append((root,1))
        
        while queue:
            
            node = queue.pop(0)
            node_val = node[0]
            node_level = node[1]
            
            if node:
                if node_val.left == None and node_val.right == None:
                    return node_level
                if node_val.left:
                    queue.append((node_val.left,node_level+1))
                if node_val.right:
                    queue.append((node_val.right,node_level+1))
            
        
        
