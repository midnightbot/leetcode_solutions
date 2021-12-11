##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        
        
        ans = []
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            ans.append([node.val])
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
                
        for x in range(len(ans)):
            ans[x].insert(0,abs(ans[x][0] - target))
        
        ans = sorted(ans, key = lambda x:x[0])
        return ans[0][1]
