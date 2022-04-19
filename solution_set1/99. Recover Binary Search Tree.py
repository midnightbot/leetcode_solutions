# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
       
        def inorder(node:TreeNode)->None:
            
            if not node:
                return
            
            
            inorder( node.left )
            
            if node.val < inorder.prev.val:
                
                
                inorder.first = inorder.prev if inorder.first is None else inorder.first
                inorder.second = node
            
            inorder.prev = node
            inorder( node.right )

        inorder.prev = TreeNode(-float('inf'))
        inorder.first = inorder.second = None
        inorder(root)
        inorder.first.val, inorder.second.val = inorder.second.val, inorder.first.val
