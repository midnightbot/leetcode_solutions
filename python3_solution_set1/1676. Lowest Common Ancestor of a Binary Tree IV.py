##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        ##go on expanding till all the nodes are on the same side of the tree
        return self.expand(root,nodes)
        
        
    def expand(self,root,nodes):
        
        if root == None:
            return None
        
        elif root in nodes:
            return root
        
        left = self.expand(root.left,nodes)
        right = self.expand(root.right,nodes)
        
        if left and right:
            return root
        
        elif left:
            return left
        
        
        elif right:
            return right
            
        
        
