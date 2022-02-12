##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        self.ans = -float('inf')
        
        def expand(root):
            #print(root)
            if root is None:
                return 0,0
            
            if root.left is None and root.right is None:
                self.ans = max(self.ans, root.val)
                return root.val,1
            
            a = expand(root.left)
            b = expand(root.right)
            #print(a,b)
            self.ans = max(self.ans , (a[0]+b[0]+root.val)/(a[1]+b[1]+1),0 if a[1] == 0 else a[0]/a[1],0 if b[1] ==0 else b[0]/b[1])
            return a[0]+b[0]+root.val,a[1]+b[1]+1
        
        
        expand(root)
        
        return self.ans
