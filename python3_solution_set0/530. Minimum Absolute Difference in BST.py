##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        ans = []
        
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            
            ans.append(node.val)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
        ans = sorted(ans)
        mins = float('inf')
        
        for x in range(len(ans)-1):
            mins = min(mins, abs(ans[x]-ans[x+1]) )
            
        return mins
        
