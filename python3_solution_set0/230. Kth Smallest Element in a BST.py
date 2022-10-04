##ss
##simple heap question
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ans = []
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            heapq.heappush(ans,node.val)
            
            if node.left!=None:
                queue.append(node.left)
                
            if node.right!=None:
                queue.append(node.right)
                
        for x in range(k):
            t = heapq.heappop(ans)
            
        return t
