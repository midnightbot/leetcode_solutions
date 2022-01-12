##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        
        def insert(root):
            
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    
                else:
                    insert(root.right)
                    
            else:
                if not root.left:
                    root.left = TreeNode(val)
                    
                else:
                    insert(root.left)
                    
                    
        insert(root)
        return root
