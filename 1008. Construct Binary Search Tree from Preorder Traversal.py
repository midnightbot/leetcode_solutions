##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode()
        for x in range(len(preorder)):
            self.insert(root,preorder[x])
            
        return root.right
    
    def insert(self,root,elem):
        
        if root == None:
            #node = TreeNode()
            root = TreeNode()
            root.val = elem
            return root
            
        if root.val > elem:
            root.left = self.insert(root.left,elem)
            
            
        else:
            root.right = self.insert(root.right,elem)
            
            
        return root
        
        
