# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #print(len(root))
        if root == None:
            return []
        prev_level = [root]
        ans = []
        ans.append(root.val)
        level = []
        level.append(-1)
        while level:
            
            while prev_level:
                root = prev_level.pop(0)
                if root!=None:
                    if root.left:
                        level.append(root.left)
                    
                    if root.right:
                        level.append(root.right)
            #print(level)
                    
            if len(level) == 1 and level[0] == -1:
                level = []
                
            if len(level)!=0:
                #print(level)
                ans.append(level[len(level)-1].val)
                prev_level = level[1:len(level)]
                level = []
                level.append(-1)
            
            else:
                level = []
 
           
          
        return ans
            
                
        
