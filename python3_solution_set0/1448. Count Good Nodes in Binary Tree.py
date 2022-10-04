##ss
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.ans = 0
        self.expand(root,-float('inf'))
        return self.ans
    
    def expand(self,root,path_max):
        #print(root.val,self.ans)
        if root.val >= path_max:
            #print(root.val,"inside")
            self.ans+=1
            path_max = root.val
            if root.left:
                self.expand(root.left,path_max)
                
            if root.right:
                self.expand(root.right,path_max)
            
        else:
            if root.left:
                self.expand(root.left,path_max)
                
            if root.right:
                self.expand(root.right,path_max)
        #print(root.val,self.ans) 
        

            
        
        
