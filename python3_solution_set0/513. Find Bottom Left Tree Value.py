# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        this_level = [root]
        
        next_level = []
        
        
        left_child = [] #key level number 
        priority = []
        left_child.append(root.val)
        priority.append(0)
        if root.left == None and root.right == None:
            return root.val
        level = 0
        while (len(this_level))!=0:
            level+=1
            
            temp  = []
            
            for x in this_level:
                if x.left:
                    #left_child.append((level,x.left.val))
                    left_child.append(x.left.val)
                    priority.append(level)
                    #left_child[level] = x.left.val
                    next_level.append(x.left)
                
                if x.right:
                    left_child.append(x.right.val)
                    priority.append(level)
                    next_level.append(x.right)
                
                
            this_level = next_level
            next_level = []
            
            
        #print(left_child)
        #print(priority)
        
        temps = priority.index(max(priority))
        return left_child[temps]
            
        
                
                
        
        
