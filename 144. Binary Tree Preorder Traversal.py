# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = [root]
        ans = []
        
        if root == None:
            return []
        
        while queue:
            root = queue.pop()
            if root!=None:
                ans.append(root.val)
                
                if root.right!=None:
                    queue.append(root.right)
                    
                if root.left!=None:
                    queue.append(root.left)
                    
        return ans
        
