##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        self.ans = 0
        
        def expand(root):
            #print(root.val,self.ans)
            if root.left is None and root.right is None:
                self.ans+=1
                return True
            
            else:
                temp1 = True
                temp2 = True
                if root.left:
                    if expand(root.left) and root.left.val == root.val:
                        temp1 = True
                        
                    else:
                        #expand(root.left)
                        temp1 = False
                        
                if root.right:
                    if expand(root.right) and root.right.val == root.val:
                        temp2 = True
                        
                    else:
                        #expand(root.right)
                        temp2 = False
                        
                if temp1 and temp2:
                    self.ans+=1
                return temp1 and temp2 
                    
        expand(root)
        return self.ans
        
