##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        self.ans = 0
        return self.expands(root,root.val,root.val)
        
        
    def expands(self,root,mins,maxs): 
        
        if root == None:
            return
        
        if root!=None:
            
            self.ans = max(self.ans, abs(maxs - root.val),abs(mins-root.val))
            
            maxs = max(maxs, root.val)
            mins = min(mins, root.val)
            
            self.expands(root.left,mins,maxs)
            self.expands(root.right,mins,maxs)
            
            
        return self.ans
                
        
