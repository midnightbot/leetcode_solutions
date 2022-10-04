##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        
        def expand(root):
            #print(root,"\n")
            if root is None:
                return root
            
            if low<=root.val<=high:
                root.left = expand(root.left)
                
                root.right = expand(root.right)
                
            else:
                if expand(root.left) is not None:
                    return expand(root.left)
                return expand(root.right)
                
                
            return root
        
        return expand(root)
        
