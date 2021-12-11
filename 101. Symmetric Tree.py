##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric(root.left,root.right)
        
        
    def symmetric(self,l,r):
        #print(l,r)
        if l == None and r == None:
            return True
        
        else:
            
            if l!=None and r!=None:
                return l.val == r.val and self.symmetric(l.left,r.right) and self.symmetric(l.right,r.left)
        
        
        
