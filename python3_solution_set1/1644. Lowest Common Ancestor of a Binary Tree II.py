##ss
##same as 1676,236
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.var = [0,0]
        self.check(root,p,q)
        
        if self.var == [1,1]:
            return self.expand(root,[p,q])
        
        return None
    
    def check(self,root,p,q):

        if root!=None:
            if root == p:
                self.var[0] = 1

            elif root == q:
                self.var[1] = 1

            if root.left:
                self.check(root.left,p,q)

            if root.right:
                self.check(root.right,p,q)
                
                
                
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
            
        
