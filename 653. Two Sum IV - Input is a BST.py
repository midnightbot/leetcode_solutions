##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
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
        i =0
        j = len(ans) - 1
        
        while i<j:
            if ans[i]+ans[j] == k:
                return True
            
            elif ans[i]+ans[j] > k:
                j-=1
                
            else:
                i+=1
                
        return False
        
