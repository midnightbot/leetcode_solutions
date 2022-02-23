##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ##inorder traversal is in ascending order
        
        self.ans = []
        
        def inorder(root):
            if root is not None:
                
                
                if root.left:
                    inorder(root.left)
                self.ans.append(root.val)
                
                if root.right:
                    inorder(root.right)
                    
        inorder(root)
        for x in range(1,len(self.ans)):
            if self.ans[x] <= self.ans[x-1]:
                return False
            
            
        return True
        
