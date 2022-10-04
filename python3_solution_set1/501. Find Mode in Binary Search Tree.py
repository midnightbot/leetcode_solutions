# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.result = set()
        self.maxcount = 0
        self.prev = root.val
        self.curr = 0
        def expand(root):
            if root is None:
                return
            
            expand(root.left)
            
            if root.val == self.prev:
                self.curr+=1
                
            else:
                self.curr = 1
                
            if self.curr == self.maxcount:
                self.result.append(root.val)
                
            elif self.curr > self.maxcount:
                self.maxcount = self.curr
                self.result = []
                self.result.append(root.val)
                
            self.prev = root.val
            expand(root.right)
            
            
                
            
        expand(root)
        return self.result
        
