# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        if root == None:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
            
        else:
            if root.left == None: ## root may have one child (that is right child)
                return root.right
            if root.right == None: ## root may have one child (that is left child)
                return root.left
            
            else: ## root has both child 
                ##find minimum from right subtree and replace this key node with that value and then delete that fromm right subtree recursively
                root.val = self.find_mins(root.right)
                root.right = self.deleteNode(root.right,root.val)
                
        return root   
    def find_mins(self,root): ##finds minimum of a subtree
        if root == None:
            return -1
        
        if root.left == None:
            return root.val
        
        return self.find_mins(root.left)
        
