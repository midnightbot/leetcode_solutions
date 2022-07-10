##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        @cache
        def find_ans(node):
            if node.left is None and node.right is None:
                if node.val == 1:
                    return True
                return False
            
            else:
                if node.val == 2:
                    return find_ans(node.left) or find_ans(node.right)
                
                return find_ans(node.left) and find_ans(node.right)
                
                
        return find_ans(root)
        
