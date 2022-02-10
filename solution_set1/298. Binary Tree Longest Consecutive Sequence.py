##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        self.makeseq(root,root.val-1,0)
        return self.ans
    def makeseq(self,root,prev,count):
        #print(count,root.val)
        self.ans = max(self.ans,count)
        if root is not None and root.val == prev+1:
            
            if root.left:
                self.makeseq(root.left,root.val,count+1)
                
            if root.right:
                self.makeseq(root.right,root.val,count+1)
                
            self.ans = max(self.ans,count+1)
                
        elif root is not None:
            
            if root.left:
                self.makeseq(root.left,root.val,1)
                
            if root.right:
                self.makeseq(root.right,root.val,1)
                
        
