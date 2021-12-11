##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        ans  = []
        
        queue = [root1,root2]
        
        while queue:
            node = queue.pop()
            if node!=None:
                ans.append(node.val)
            
            if node and node.left:
                queue.append(node.left)
                
            if node and node.right:
                queue.append(node.right)
                
                
        return sorted(ans)
        
