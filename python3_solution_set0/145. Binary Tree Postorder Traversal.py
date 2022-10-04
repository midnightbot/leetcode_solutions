# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        queue = [root]
        ans = []
        
        while queue:
            root = queue.pop()
            if root!=None:
                if root.left!=None:
                    queue.append(root.left)
                if root.right!=None:
                    queue.append(root.right)
                
                
                
                if root!=None:
                    ans.append(root.val)
                
        ans = ans[::-1]
        return ans
        
